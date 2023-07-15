from collections.abc import Mapping
from typing import Any, Dict, Iterator, List, Optional, Tuple, TypedDict, Union, Literal

RemarkType = Literal["a", "x", "s", "m", "p", "e"]

class Remark(TypedDict):
    rule_id: str
    type: RemarkType
    range_start: Optional[int]
    range_end: Optional[int]

class Meta:
    def __init__(self, meta: Optional[Dict[str, Any]] = None, path: Optional[List[str]] = None):
        self._meta: Dict[str, Any] = {} if meta is None else meta
        self._path: List[str] = path or []

    def enter(self, *path: Any) -> "Meta":
        return Meta(self._meta, path=self._path + [str(p) for p in path])

    @property
    def path(self) -> str:
        return ".".join(self._path)

    def raw(self) -> Dict[str, Any]:
        meta = self._meta
        for key in self._path:
            meta = meta.get(key) or {}
        return meta

    def get(self) -> Dict[str, Any]:
        return self.raw().get("") or {}

    def create(self) -> Dict[str, Any]:
        meta = self._meta
        for key in self._path + [""]:
            if key not in meta or meta[key] is None:
                meta[key] = {}
            meta = meta[key]
        return meta

    def merge(self, other: "Meta") -> Optional[Dict[str, Any]]:
        other = other.get()
        if not other:
            return None
        meta = self.create()
        err = meta.get("err")
        meta.update(other)
        if err and other.get("err"):
            meta["err"] = err + other["err"]
        return meta

    def iter_errors(self) -> Iterator[Tuple[Union[str, List[str]], Dict[str, Any]]]:
        return (
            ([err, {}] if isinstance(err, str) else err)
            for err in self.get().get("err") or ()
        )

    def get_event_errors(self) -> List[Dict[str, Any]]:
        errors = []
        value = self.get().get("val")
        for error, data in self.iter_errors():
            eventerror = dict(data)
            eventerror["type"] = error
            if self._path:
                eventerror["name"] = ".".join(self._path)
            if value is not None:
                eventerror["value"] = value
                value = None
            errors.append(eventerror)
        return errors

    def add_error(self, error: Any, value: Optional[Any] = None, data: Optional[Dict[str, Any]] = None) -> None:
        meta = self.create()
        if "err" not in meta or meta["err"] is None:
            meta["err"] = []
        error = str(error)
        if isinstance(data, Mapping):
            error = [error, dict(data)]
        meta["err"].append(error)
        if value is not None:
            meta["val"] = value

    def add_remark(self, rem: Remark, value: Optional[Any] = None) -> None:
        meta = self.create()
        if "rem" not in meta or meta["rem"] is None:
            meta["rem"] = []
        rem_list: List[Union[str, int]] = [rem["rule_id"], rem["type"]]
        range_start = rem.get("range_start")
        if range_start is not None:
            rem_list.append(range_start)
        range_end = rem.get("range_end")
        if range_end is not None:
            rem_list.append(range_end)
        meta["rem"].append(rem_list)
        if value is not None:
            meta["val"] = value

    def __iter__(self) -> Iterator["Meta"]:
        for key in self.raw():
            if key != "":
                yield self.enter(key)
