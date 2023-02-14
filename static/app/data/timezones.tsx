import styled from '@emotion/styled';
import groupBy from 'lodash/groupBy';

import {SelectValue} from 'sentry/types';

type TimezoneGroup =
  | null
  | 'Other'
  | 'US/Canada'
  | 'America'
  | 'Europe'
  | 'Australia'
  | 'Asia'
  | 'Indian'
  | 'Africa'
  | 'Pacific'
  | 'Atlantic'
  | 'Antarctica'
  | 'Arctic';

const timezones: [
  group: TimezoneGroup,
  offsetLabel: string,
  value: string,
  label: string
][] = [
  ['Other', '+0', 'UTC', 'UTC'],
  ['Other', '+0', 'GMT', 'GMT'],

  // Group US higher-ish since
  ['US/Canada', '-5', 'US/Eastern', 'Eastern'],
  ['US/Canada', '-6', 'US/Central', 'Central'],
  ['US/Canada', '-7', 'US/Arizona', 'Arizona'],
  ['US/Canada', '-7', 'US/Mountain', 'Mountain'],
  ['US/Canada', '-8', 'US/Pacific', 'Pacific'],
  ['US/Canada', '-9', 'US/Alaska', 'Alaska'],
  ['US/Canada', '-10', 'US/Hawaii', 'Hawaii'],
  ['US/Canada', '-3:30', 'Canada/Newfoundland', 'Newfoundland'],
  ['US/Canada', '-4', 'Canada/Atlantic', 'Atlantic'],
  ['US/Canada', '-5', 'Canada/Eastern', 'Canadian Eastern'],
  ['US/Canada', '-6', 'Canada/Central', 'Canadian Central'],
  ['US/Canada', '-7', 'Canada/Mountain', 'Canadian Mountain'],
  ['US/Canada', '-8', 'Canada/Pacific', 'Canadian Pacific'],

  ['America', '+0', 'America/Danmarkshavn', 'Danmarkshavn'],
  ['America', '-1', 'America/Scoresbysund', 'Scoresbysund'],
  ['America', '-2', 'America/Noronha', 'Noronha'],
  ['America', '-3', 'America/Araguaina', 'Araguaina'],
  ['America', '-3', 'America/Argentina/Buenos_Aires', 'Argentina / Buenos Aires'],
  ['America', '-3', 'America/Argentina/Catamarca', 'Argentina / Catamarca'],
  ['America', '-3', 'America/Argentina/Cordoba', 'Argentina / Cordoba'],
  ['America', '-3', 'America/Argentina/Jujuy', 'Argentina / Jujuy'],
  ['America', '-3', 'America/Argentina/La_Rioja', 'Argentina / La Rioja'],
  ['America', '-3', 'America/Argentina/Mendoza', 'Argentina / Mendoza'],
  ['America', '-3', 'America/Argentina/Rio_Gallegos', 'Argentina / Rio Gallegos'],
  ['America', '-3', 'America/Argentina/Salta', 'Argentina / Salta'],
  ['America', '-3', 'America/Argentina/San_Juan', 'Argentina / San Juan'],
  ['America', '-3', 'America/Argentina/San_Luis', 'Argentina / San Luis'],
  ['America', '-3', 'America/Argentina/Tucuman', 'Argentina / Tucuman'],
  ['America', '-3', 'America/Argentina/Ushuaia', 'Argentina / Ushuaia'],
  ['America', '-3', 'America/Asuncion', 'Asuncion'],
  ['America', '-3', 'America/Bahia', 'Bahia'],
  ['America', '-3', 'America/Belem', 'Belem'],
  ['America', '-3', 'America/Campo_Grande', 'Campo Grande'],
  ['America', '-3', 'America/Cayenne', 'Cayenne'],
  ['America', '-3', 'America/Cuiaba', 'Cuiaba'],
  ['America', '-3', 'America/Fortaleza', 'Fortaleza'],
  ['America', '-3', 'America/Godthab', 'Godthab'],
  ['America', '-3', 'America/Maceio', 'Maceio'],
  ['America', '-3', 'America/Miquelon', 'Miquelon'],
  ['America', '-3', 'America/Montevideo', 'Montevideo'],
  ['America', '-3', 'America/Paramaribo', 'Paramaribo'],
  ['America', '-3', 'America/Recife', 'Recife'],
  ['America', '-3', 'America/Santarem', 'Santarem'],
  ['America', '-3', 'America/Santiago', 'Santiago'],
  ['America', '-3', 'America/Sao_Paulo', 'Sao Paulo'],
  ['America', '-3:30', 'America/St_Johns', 'St Johns'],
  ['America', '-4', 'America/Anguilla', 'Anguilla'],
  ['America', '-4', 'America/Antigua', 'Antigua'],
  ['America', '-4', 'America/Aruba', 'Aruba'],
  ['America', '-4', 'America/Barbados', 'Barbados'],
  ['America', '-4', 'America/Blanc-Sablon', 'Blanc-Sablon'],
  ['America', '-4', 'America/Boa_Vista', 'Boa Vista'],
  ['America', '-4', 'America/Caracas', 'Caracas'],
  ['America', '-4', 'America/Curacao', 'Curacao'],
  ['America', '-4', 'America/Dominica', 'Dominica'],
  ['America', '-4', 'America/Glace_Bay', 'Glace Bay'],
  ['America', '-4', 'America/Goose_Bay', 'Goose Bay'],
  ['America', '-4', 'America/Grenada', 'Grenada'],
  ['America', '-4', 'America/Guadeloupe', 'Guadeloupe'],
  ['America', '-4', 'America/Guyana', 'Guyana'],
  ['America', '-4', 'America/Halifax', 'Halifax'],
  ['America', '-4', 'America/Kralendijk', 'Kralendijk'],
  ['America', '-4', 'America/La_Paz', 'La Paz'],
  ['America', '-4', 'America/Lower_Princes', 'Lower Princes'],
  ['America', '-4', 'America/Manaus', 'Manaus'],
  ['America', '-4', 'America/Marigot', 'Marigot'],
  ['America', '-4', 'America/Martinique', 'Martinique'],
  ['America', '-4', 'America/Moncton', 'Moncton'],
  ['America', '-4', 'America/Montserrat', 'Montserrat'],
  ['America', '-4', 'America/Port_of_Spain', 'Port of Spain'],
  ['America', '-4', 'America/Porto_Velho', 'Porto Velho'],
  ['America', '-4', 'America/Puerto_Rico', 'Puerto Rico'],
  ['America', '-4', 'America/Santo_Domingo', 'Santo Domingo'],
  ['America', '-4', 'America/St_Barthelemy', 'St Barthelemy'],
  ['America', '-4', 'America/St_Kitts', 'St Kitts'],
  ['America', '-4', 'America/St_Lucia', 'St Lucia'],
  ['America', '-4', 'America/St_Thomas', 'St Thomas'],
  ['America', '-4', 'America/St_Vincent', 'St Vincent'],
  ['America', '-4', 'America/Thule', 'Thule'],
  ['America', '-4', 'America/Tortola', 'Tortola'],
  ['America', '-5', 'America/Atikokan', 'Atikokan'],
  ['America', '-5', 'America/Bogota', 'Bogota'],
  ['America', '-5', 'America/Cancun', 'Cancun'],
  ['America', '-5', 'America/Cayman', 'Cayman'],
  ['America', '-5', 'America/Detroit', 'Detroit'],
  ['America', '-5', 'America/Eirunepe', 'Eirunepe'],
  ['America', '-5', 'America/Grand_Turk', 'Grand Turk'],
  ['America', '-5', 'America/Guayaquil', 'Guayaquil'],
  ['America', '-5', 'America/Havana', 'Havana'],
  ['America', '-5', 'America/Indiana/Indianapolis', 'Indiana / Indianapolis'],
  ['America', '-5', 'America/Indiana/Marengo', 'Indiana / Marengo'],
  ['America', '-5', 'America/Indiana/Petersburg', 'Indiana / Petersburg'],
  ['America', '-5', 'America/Indiana/Vevay', 'Indiana / Vevay'],
  ['America', '-5', 'America/Indiana/Vincennes', 'Indiana / Vincennes'],
  ['America', '-5', 'America/Indiana/Winamac', 'Indiana / Winamac'],
  ['America', '-5', 'America/Iqaluit', 'Iqaluit'],
  ['America', '-5', 'America/Jamaica', 'Jamaica'],
  ['America', '-5', 'America/Kentucky/Louisville', 'Kentucky / Louisville'],
  ['America', '-5', 'America/Kentucky/Monticello', 'Kentucky / Monticello'],
  ['America', '-5', 'America/Lima', 'Lima'],
  ['America', '-5', 'America/Nassau', 'Nassau'],
  ['America', '-5', 'America/New_York', 'New York'],
  ['America', '-5', 'America/Nipigon', 'Nipigon'],
  ['America', '-5', 'America/Panama', 'Panama'],
  ['America', '-5', 'America/Pangnirtung', 'Pangnirtung'],
  ['America', '-5', 'America/Port-au-Prince', 'Port-au-Prince'],
  ['America', '-5', 'America/Rio_Branco', 'Rio Branco'],
  ['America', '-5', 'America/Thunder_Bay', 'Thunder Bay'],
  ['America', '-5', 'America/Toronto', 'Toronto'],
  ['America', '-6', 'America/Bahia_Banderas', 'Bahia Banderas'],
  ['America', '-6', 'America/Belize', 'Belize'],
  ['America', '-6', 'America/Chicago', 'Chicago'],
  ['America', '-6', 'America/Costa_Rica', 'Costa Rica'],
  ['America', '-6', 'America/El_Salvador', 'El Salvador'],
  ['America', '-6', 'America/Guatemala', 'Guatemala'],
  ['America', '-6', 'America/Indiana/Knox', 'Indiana / Knox'],
  ['America', '-6', 'America/Indiana/Tell_City', 'Indiana / Tell City'],
  ['America', '-6', 'America/Managua', 'Managua'],
  ['America', '-6', 'America/Matamoros', 'Matamoros'],
  ['America', '-6', 'America/Menominee', 'Menominee'],
  ['America', '-6', 'America/Merida', 'Merida'],
  ['America', '-6', 'America/Mexico_City', 'Mexico City'],
  ['America', '-6', 'America/Monterrey', 'Monterrey'],
  ['America', '-6', 'America/North_Dakota/Beulah', 'North Dakota / Beulah'],
  ['America', '-6', 'America/North_Dakota/Center', 'North Dakota / Center'],
  ['America', '-6', 'America/North_Dakota/New_Salem', 'North Dakota / New Salem'],
  ['America', '-6', 'America/Rainy_River', 'Rainy River'],
  ['America', '-6', 'America/Rankin_Inlet', 'Rankin Inlet'],
  ['America', '-6', 'America/Regina', 'Regina'],
  ['America', '-6', 'America/Resolute', 'Resolute'],
  ['America', '-6', 'America/Swift_Current', 'Swift Current'],
  ['America', '-6', 'America/Tegucigalpa', 'Tegucigalpa'],
  ['America', '-6', 'America/Winnipeg', 'Winnipeg'],
  ['America', '-7', 'America/Boise', 'Boise'],
  ['America', '-7', 'America/Cambridge_Bay', 'Cambridge Bay'],
  ['America', '-7', 'America/Chihuahua', 'Chihuahua'],
  ['America', '-7', 'America/Creston', 'Creston'],
  ['America', '-7', 'America/Dawson_Creek', 'Dawson Creek'],
  ['America', '-7', 'America/Denver', 'Denver'],
  ['America', '-7', 'America/Edmonton', 'Edmonton'],
  ['America', '-7', 'America/Fort_Nelson', 'Fort Nelson'],
  ['America', '-7', 'America/Hermosillo', 'Hermosillo'],
  ['America', '-7', 'America/Inuvik', 'Inuvik'],
  ['America', '-7', 'America/Mazatlan', 'Mazatlan'],
  ['America', '-7', 'America/Ojinaga', 'Ojinaga'],
  ['America', '-7', 'America/Phoenix', 'Phoenix'],
  ['America', '-7', 'America/Yellowknife', 'Yellowknife'],
  ['America', '-8', 'America/Dawson', 'Dawson'],
  ['America', '-8', 'America/Los_Angeles', 'Los Angeles'],
  ['America', '-8', 'America/Tijuana', 'Tijuana'],
  ['America', '-8', 'America/Vancouver', 'Vancouver'],
  ['America', '-8', 'America/Whitehorse', 'Whitehorse'],
  ['America', '-9', 'America/Anchorage', 'Anchorage'],
  ['America', '-9', 'America/Juneau', 'Juneau'],
  ['America', '-9', 'America/Metlakatla', 'Metlakatla'],
  ['America', '-9', 'America/Nome', 'Nome'],
  ['America', '-9', 'America/Sitka', 'Sitka'],
  ['America', '-9', 'America/Yakutat', 'Yakutat'],
  ['America', '-10', 'America/Adak', 'Adak'],

  ['Europe', '+0', 'Europe/Dublin', 'Dublin'],
  ['Europe', '+0', 'Europe/Guernsey', 'Guernsey'],
  ['Europe', '+0', 'Europe/Isle_of_Man', 'Isle of Man'],
  ['Europe', '+0', 'Europe/Jersey', 'Jersey'],
  ['Europe', '+0', 'Europe/Lisbon', 'Lisbon'],
  ['Europe', '+0', 'Europe/London', 'London'],
  ['Europe', '+1', 'Europe/Amsterdam', 'Amsterdam'],
  ['Europe', '+1', 'Europe/Andorra', 'Andorra'],
  ['Europe', '+1', 'Europe/Belgrade', 'Belgrade'],
  ['Europe', '+1', 'Europe/Berlin', 'Berlin'],
  ['Europe', '+1', 'Europe/Bratislava', 'Bratislava'],
  ['Europe', '+1', 'Europe/Brussels', 'Brussels'],
  ['Europe', '+1', 'Europe/Budapest', 'Budapest'],
  ['Europe', '+1', 'Europe/Busingen', 'Busingen'],
  ['Europe', '+1', 'Europe/Copenhagen', 'Copenhagen'],
  ['Europe', '+1', 'Europe/Gibraltar', 'Gibraltar'],
  ['Europe', '+1', 'Europe/Ljubljana', 'Ljubljana'],
  ['Europe', '+1', 'Europe/Luxembourg', 'Luxembourg'],
  ['Europe', '+1', 'Europe/Madrid', 'Madrid'],
  ['Europe', '+1', 'Europe/Malta', 'Malta'],
  ['Europe', '+1', 'Europe/Monaco', 'Monaco'],
  ['Europe', '+1', 'Europe/Oslo', 'Oslo'],
  ['Europe', '+1', 'Europe/Paris', 'Paris'],
  ['Europe', '+1', 'Europe/Podgorica', 'Podgorica'],
  ['Europe', '+1', 'Europe/Prague', 'Prague'],
  ['Europe', '+1', 'Europe/Rome', 'Rome'],
  ['Europe', '+1', 'Europe/San_Marino', 'San Marino'],
  ['Europe', '+1', 'Europe/Sarajevo', 'Sarajevo'],
  ['Europe', '+1', 'Europe/Skopje', 'Skopje'],
  ['Europe', '+1', 'Europe/Stockholm', 'Stockholm'],
  ['Europe', '+1', 'Europe/Tirane', 'Tirane'],
  ['Europe', '+1', 'Europe/Vaduz', 'Vaduz'],
  ['Europe', '+1', 'Europe/Vatican', 'Vatican'],
  ['Europe', '+1', 'Europe/Vienna', 'Vienna'],
  ['Europe', '+1', 'Europe/Warsaw', 'Warsaw'],
  ['Europe', '+1', 'Europe/Zagreb', 'Zagreb'],
  ['Europe', '+1', 'Europe/Zurich', 'Zurich'],
  ['Europe', '+2', 'Europe/Athens', 'Athens'],
  ['Europe', '+2', 'Europe/Bucharest', 'Bucharest'],
  ['Europe', '+2', 'Europe/Chisinau', 'Chisinau'],
  ['Europe', '+2', 'Europe/Helsinki', 'Helsinki'],
  ['Europe', '+2', 'Europe/Kaliningrad', 'Kaliningrad'],
  ['Europe', '+2', 'Europe/Mariehamn', 'Mariehamn'],
  ['Europe', '+2', 'Europe/Riga', 'Riga'],
  ['Europe', '+2', 'Europe/Sofia', 'Sofia'],
  ['Europe', '+2', 'Europe/Tallinn', 'Tallinn'],
  ['Europe', '+2', 'Europe/Uzhgorod', 'Uzhgorod'],
  ['Europe', '+2', 'Europe/Vilnius', 'Vilnius'],
  ['Europe', '+2', 'Europe/Zaporozhye', 'Zaporozhye'],
  ['Europe', '+3', 'Europe/Istanbul', 'Istanbul'],
  ['Europe', '+3', 'Europe/Kiev', 'Kiev'],
  ['Europe', '+3', 'Europe/Minsk', 'Minsk'],
  ['Europe', '+3', 'Europe/Moscow', 'Moscow'],
  ['Europe', '+3', 'Europe/Simferopol', 'Simferopol'],
  ['Europe', '+4', 'Europe/Samara', 'Samara'],
  ['Europe', '+4', 'Europe/Volgograd', 'Volgograd'],

  ['Asia', '+2', 'Asia/Amman', 'Amman'],
  ['Asia', '+2', 'Asia/Beirut', 'Beirut'],
  ['Asia', '+2', 'Asia/Damascus', 'Damascus'],
  ['Asia', '+2', 'Asia/Gaza', 'Gaza'],
  ['Asia', '+2', 'Asia/Hebron', 'Hebron'],
  ['Asia', '+2', 'Asia/Jerusalem', 'Jerusalem'],
  ['Asia', '+2', 'Asia/Nicosia', 'Nicosia'],
  ['Asia', '+3', 'Asia/Aden', 'Aden'],
  ['Asia', '+3', 'Asia/Baghdad', 'Baghdad'],
  ['Asia', '+3', 'Asia/Bahrain', 'Bahrain'],
  ['Asia', '+3', 'Asia/Kuwait', 'Kuwait'],
  ['Asia', '+3', 'Asia/Qatar', 'Qatar'],
  ['Asia', '+3', 'Asia/Riyadh', 'Riyadh'],
  ['Asia', '+3:30', 'Asia/Tehran', 'Tehran'],
  ['Asia', '+4', 'Asia/Baku', 'Baku'],
  ['Asia', '+4', 'Asia/Dubai', 'Dubai'],
  ['Asia', '+4', 'Asia/Muscat', 'Muscat'],
  ['Asia', '+4', 'Asia/Tbilisi', 'Tbilisi'],
  ['Asia', '+4', 'Asia/Yerevan', 'Yerevan'],
  ['Asia', '+4:30', 'Asia/Kabul', 'Kabul'],
  ['Asia', '+5', 'Asia/Aqtau', 'Aqtau'],
  ['Asia', '+5', 'Asia/Aqtobe', 'Aqtobe'],
  ['Asia', '+5', 'Asia/Ashgabat', 'Ashgabat'],
  ['Asia', '+5', 'Asia/Dushanbe', 'Dushanbe'],
  ['Asia', '+5', 'Asia/Karachi', 'Karachi'],
  ['Asia', '+5', 'Asia/Oral', 'Oral'],
  ['Asia', '+5', 'Asia/Samarkand', 'Samarkand'],
  ['Asia', '+5', 'Asia/Tashkent', 'Tashkent'],
  ['Asia', '+5', 'Asia/Yekaterinburg', 'Yekaterinburg'],
  ['Asia', '+5:30', 'Asia/Colombo', 'Colombo'],
  ['Asia', '+5:30', 'Asia/Kolkata', 'Kolkata'],
  ['Asia', '+5:45', 'Asia/Kathmandu', 'Kathmandu'],
  ['Asia', '+6', 'Asia/Almaty', 'Almaty'],
  ['Asia', '+6', 'Asia/Bishkek', 'Bishkek'],
  ['Asia', '+6', 'Asia/Dhaka', 'Dhaka'],
  ['Asia', '+6', 'Asia/Novosibirsk', 'Novosibirsk'],
  ['Asia', '+6', 'Asia/Omsk', 'Omsk'],
  ['Asia', '+6', 'Asia/Qyzylorda', 'Qyzylorda'],
  ['Asia', '+6', 'Asia/Thimphu', 'Thimphu'],
  ['Asia', '+6', 'Asia/Urumqi', 'Urumqi'],
  ['Asia', '+6:30', 'Asia/Rangoon', 'Rangoon'],
  ['Asia', '+7', 'Asia/Bangkok', 'Bangkok'],
  ['Asia', '+7', 'Asia/Ho_Chi_Minh', 'Ho Chi Minh'],
  ['Asia', '+7', 'Asia/Hovd', 'Hovd'],
  ['Asia', '+7', 'Asia/Jakarta', 'Jakarta'],
  ['Asia', '+7', 'Asia/Krasnoyarsk', 'Krasnoyarsk'],
  ['Asia', '+7', 'Asia/Novokuznetsk', 'Novokuznetsk'],
  ['Asia', '+7', 'Asia/Phnom_Penh', 'Phnom Penh'],
  ['Asia', '+7', 'Asia/Pontianak', 'Pontianak'],
  ['Asia', '+7', 'Asia/Vientiane', 'Vientiane'],
  ['Asia', '+8', 'Asia/Brunei', 'Brunei'],
  ['Asia', '+8', 'Asia/Choibalsan', 'Choibalsan'],
  ['Asia', '+8', 'Asia/Hong_Kong', 'Hong Kong'],
  ['Asia', '+8', 'Asia/Irkutsk', 'Irkutsk'],
  ['Asia', '+8', 'Asia/Kuala_Lumpur', 'Kuala Lumpur'],
  ['Asia', '+8', 'Asia/Kuching', 'Kuching'],
  ['Asia', '+8', 'Asia/Macau', 'Macau'],
  ['Asia', '+8', 'Asia/Makassar', 'Makassar'],
  ['Asia', '+8', 'Asia/Manila', 'Manila'],
  ['Asia', '+8', 'Asia/Shanghai', 'Shanghai'],
  ['Asia', '+8', 'Asia/Singapore', 'Singapore'],
  ['Asia', '+8', 'Asia/Taipei', 'Taipei'],
  ['Asia', '+8', 'Asia/Ulaanbaatar', 'Ulaanbaatar'],
  ['Asia', '+9', 'Asia/Chita', 'Chita'],
  ['Asia', '+9', 'Asia/Dili', 'Dili'],
  ['Asia', '+9', 'Asia/Jayapura', 'Jayapura'],
  ['Asia', '+9', 'Asia/Khandyga', 'Khandyga'],
  ['Asia', '+9', 'Asia/Pyongyang', 'Pyongyang'],
  ['Asia', '+9', 'Asia/Seoul', 'Seoul'],
  ['Asia', '+9', 'Asia/Tokyo', 'Tokyo'],
  ['Asia', '+9', 'Asia/Yakutsk', 'Yakutsk'],
  ['Asia', '+10', 'Asia/Magadan', 'Magadan'],
  ['Asia', '+10', 'Asia/Sakhalin', 'Sakhalin'],
  ['Asia', '+10', 'Asia/Ust-Nera', 'Ust-Nera'],
  ['Asia', '+10', 'Asia/Vladivostok', 'Vladivostok'],
  ['Asia', '+11', 'Asia/Srednekolymsk', 'Srednekolymsk'],
  ['Asia', '+12', 'Asia/Anadyr', 'Anadyr'],
  ['Asia', '+12', 'Asia/Kamchatka', 'Kamchatka'],

  ['Australia', '+8', 'Australia/Perth', 'Perth'],
  ['Australia', '+8:45', 'Australia/Eucla', 'Eucla'],
  ['Australia', '+9:30', 'Australia/Darwin', 'Darwin'],
  ['Australia', '+10', 'Australia/Brisbane', 'Brisbane'],
  ['Australia', '+10', 'Australia/Lindeman', 'Lindeman'],
  ['Australia', '+10:30', 'Australia/Adelaide', 'Adelaide'],
  ['Australia', '+10', 'Australia/Broken_Hill', 'Broken Hill'],
  ['Australia', '+11', 'Australia/Currie', 'Currie'],
  ['Australia', '+11', 'Australia/Hobart', 'Hobart'],
  ['Australia', '+11', 'Australia/Lord_Howe', 'Lord_Howe'],
  ['Australia', '+11', 'Australia/Melbourne', 'Melbourne'],
  ['Australia', '+11', 'Australia/Sydney', 'Sydney'],

  ['Indian', '+3', 'Indian/Antananarivo', 'Antananarivo'],
  ['Indian', '+3', 'Indian/Comoro', 'Comoro'],
  ['Indian', '+3', 'Indian/Mayotte', 'Mayotte'],
  ['Indian', '+4', 'Indian/Mahe', 'Mahe'],
  ['Indian', '+4', 'Indian/Mauritius', 'Mauritius'],
  ['Indian', '+4', 'Indian/Reunion', 'Reunion'],
  ['Indian', '+5', 'Indian/Kerguelen', 'Kerguelen'],
  ['Indian', '+5', 'Indian/Maldives', 'Maldives'],
  ['Indian', '+6', 'Indian/Chagos', 'Chagos'],
  ['Indian', '+6:30', 'Indian/Cocos', 'Cocos'],
  ['Indian', '+7', 'Indian/Christmas', 'Christmas'],

  ['Africa', '+0', 'Africa/Abidjan', 'Abidjan'],
  ['Africa', '+0', 'Africa/Accra', 'Accra'],
  ['Africa', '+0', 'Africa/Bamako', 'Bamako'],
  ['Africa', '+0', 'Africa/Banjul', 'Banjul'],
  ['Africa', '+0', 'Africa/Bissau', 'Bissau'],
  ['Africa', '+0', 'Africa/Casablanca', 'Casablanca'],
  ['Africa', '+0', 'Africa/Conakry', 'Conakry'],
  ['Africa', '+0', 'Africa/Dakar', 'Dakar'],
  ['Africa', '+0', 'Africa/El_Aaiun', 'El Aaiun'],
  ['Africa', '+0', 'Africa/Freetown', 'Freetown'],
  ['Africa', '+0', 'Africa/Lome', 'Lome'],
  ['Africa', '+0', 'Africa/Monrovia', 'Monrovia'],
  ['Africa', '+0', 'Africa/Nouakchott', 'Nouakchott'],
  ['Africa', '+0', 'Africa/Ouagadougou', 'Ouagadougou'],
  ['Africa', '+0', 'Africa/Sao_Tome', 'Sao Tome'],
  ['Africa', '+1', 'Africa/Algiers', 'Algiers'],
  ['Africa', '+1', 'Africa/Bangui', 'Bangui'],
  ['Africa', '+1', 'Africa/Brazzaville', 'Brazzaville'],
  ['Africa', '+1', 'Africa/Ceuta', 'Ceuta'],
  ['Africa', '+1', 'Africa/Douala', 'Douala'],
  ['Africa', '+1', 'Africa/Kinshasa', 'Kinshasa'],
  ['Africa', '+1', 'Africa/Lagos', 'Lagos'],
  ['Africa', '+1', 'Africa/Libreville', 'Libreville'],
  ['Africa', '+1', 'Africa/Luanda', 'Luanda'],
  ['Africa', '+1', 'Africa/Malabo', 'Malabo'],
  ['Africa', '+1', 'Africa/Ndjamena', 'Ndjamena'],
  ['Africa', '+1', 'Africa/Niamey', 'Niamey'],
  ['Africa', '+1', 'Africa/Porto-Novo', 'Porto-Novo'],
  ['Africa', '+1', 'Africa/Tunis', 'Tunis'],
  ['Africa', '+2', 'Africa/Blantyre', 'Blantyre'],
  ['Africa', '+2', 'Africa/Bujumbura', 'Bujumbura'],
  ['Africa', '+2', 'Africa/Cairo', 'Cairo'],
  ['Africa', '+2', 'Africa/Gaborone', 'Gaborone'],
  ['Africa', '+2', 'Africa/Harare', 'Harare'],
  ['Africa', '+2', 'Africa/Johannesburg', 'Johannesburg'],
  ['Africa', '+2', 'Africa/Juba', 'Juba'],
  ['Africa', '+2', 'Africa/Khartoum', 'Khartoum'],
  ['Africa', '+2', 'Africa/Kigali', 'Kigali'],
  ['Africa', '+2', 'Africa/Lubumbashi', 'Lubumbashi'],
  ['Africa', '+2', 'Africa/Lusaka', 'Lusaka'],
  ['Africa', '+2', 'Africa/Maputo', 'Maputo'],
  ['Africa', '+2', 'Africa/Maseru', 'Maseru'],
  ['Africa', '+2', 'Africa/Mbabane', 'Mbabane'],
  ['Africa', '+2', 'Africa/Tripoli', 'Tripoli'],
  ['Africa', '+2', 'Africa/Windhoek', 'Windhoek'],
  ['Africa', '+3', 'Africa/Addis_Ababa', 'Addis Ababa'],
  ['Africa', '+3', 'Africa/Asmara', 'Asmara'],
  ['Africa', '+3', 'Africa/Dar_es_Salaam', 'Dar es Salaam'],
  ['Africa', '+3', 'Africa/Djibouti', 'Djibouti'],
  ['Africa', '+3', 'Africa/Kampala', 'Kampala'],
  ['Africa', '+3', 'Africa/Mogadishu', 'Mogadishu'],
  ['Africa', '+3', 'Africa/Nairobi', 'Nairobi'],

  ['Pacific', '+9', 'Pacific/Palau', 'Palau'],
  ['Pacific', '+10', 'Pacific/Chuuk', 'Chuuk'],
  ['Pacific', '+10', 'Pacific/Guam', 'Guam'],
  ['Pacific', '+10', 'Pacific/Port_Moresby', 'Port Moresby'],
  ['Pacific', '+10', 'Pacific/Saipan', 'Saipan'],
  ['Pacific', '+11', 'Pacific/Bougainville', 'Bougainville'],
  ['Pacific', '+11', 'Pacific/Efate', 'Efate'],
  ['Pacific', '+11', 'Pacific/Guadalcanal', 'Guadalcanal'],
  ['Pacific', '+11', 'Pacific/Kosrae', 'Kosrae'],
  ['Pacific', '+11', 'Pacific/Norfolk', 'Norfolk'],
  ['Pacific', '+11', 'Pacific/Noumea', 'Noumea'],
  ['Pacific', '+11', 'Pacific/Pohnpei', 'Pohnpei'],
  ['Pacific', '+12', 'Pacific/Funafuti', 'Funafuti'],
  ['Pacific', '+12', 'Pacific/Kwajalein', 'Kwajalein'],
  ['Pacific', '+12', 'Pacific/Majuro', 'Majuro'],
  ['Pacific', '+12', 'Pacific/Nauru', 'Nauru'],
  ['Pacific', '+12', 'Pacific/Tarawa', 'Tarawa'],
  ['Pacific', '+12', 'Pacific/Wake', 'Wake'],
  ['Pacific', '+12', 'Pacific/Wallis', 'Wallis'],
  ['Pacific', '+13', 'Pacific/Auckland', 'Auckland'],
  ['Pacific', '+13', 'Pacific/Enderbury', 'Enderbury'],
  ['Pacific', '+13', 'Pacific/Fakaofo', 'Fakaofo'],
  ['Pacific', '+13', 'Pacific/Fiji', 'Fiji'],
  ['Pacific', '+13', 'Pacific/Tongatapu', 'Tongatapu'],
  ['Pacific', '+13:45', 'Pacific/Chatham', 'Chatham'],
  ['Pacific', '+14', 'Pacific/Apia', 'Apia'],
  ['Pacific', '+14', 'Pacific/Kiritimati', 'Kiritimati'],
  ['Pacific', '-5', 'Pacific/Easter', 'Easter'],
  ['Pacific', '-6', 'Pacific/Galapagos', 'Galapagos'],
  ['Pacific', '-8', 'Pacific/Pitcairn', 'Pitcairn'],
  ['Pacific', '-9', 'Pacific/Gambier', 'Gambier'],
  ['Pacific', '-9:30', 'Pacific/Marquesas', 'Marquesas'],
  ['Pacific', '-10', 'Pacific/Honolulu', 'Honolulu'],
  ['Pacific', '-10', 'Pacific/Johnston', 'Johnston'],
  ['Pacific', '-10', 'Pacific/Rarotonga', 'Rarotonga'],
  ['Pacific', '-10', 'Pacific/Tahiti', 'Tahiti'],
  ['Pacific', '-11', 'Pacific/Midway', 'Midway'],
  ['Pacific', '-11', 'Pacific/Niue', 'Niue'],
  ['Pacific', '-11', 'Pacific/Pago_Pago', 'Pago Pago'],

  ['Atlantic', '+0', 'Atlantic/Canary', 'Canary'],
  ['Atlantic', '+0', 'Atlantic/Faroe', 'Faroe'],
  ['Atlantic', '+0', 'Atlantic/Madeira', 'Madeira'],
  ['Atlantic', '+0', 'Atlantic/Reykjavik', 'Reykjavik'],
  ['Atlantic', '+0', 'Atlantic/St_Helena', 'St Helena'],
  ['Atlantic', '-1', 'Atlantic/Azores', 'Azores'],
  ['Atlantic', '-1', 'Atlantic/Cape_Verde', 'Cape Verde'],
  ['Atlantic', '-2', 'Atlantic/South_Georgia', 'South Georgia'],
  ['Atlantic', '-3', 'Atlantic/Stanley', 'Stanley'],
  ['Atlantic', '-4', 'Atlantic/Bermuda', 'Bermuda'],

  ['Antarctica', '+0', 'Antarctica/Troll', 'Troll'],
  ['Antarctica', '+3', 'Antarctica/Syowa', 'Syowa'],
  ['Antarctica', '+5', 'Antarctica/Mawson', 'Mawson'],
  ['Antarctica', '+6', 'Antarctica/Vostok', 'Vostok'],
  ['Antarctica', '+7', 'Antarctica/Davis', 'Davis'],
  ['Antarctica', '+8', 'Antarctica/Casey', 'Casey'],
  ['Antarctica', '+10', 'Antarctica/DumontDUrville', 'DumontDUrville'],
  ['Antarctica', '+11', 'Antarctica/Macquarie', 'Macquarie'],
  ['Antarctica', '+13', 'Antarctica/McMurdo', 'McMurdo'],
  ['Antarctica', '-3', 'Antarctica/Palmer', 'Palmer'],
  ['Antarctica', '-3', 'Antarctica/Rothera', 'Rothera'],
  ['Arctic', '+1', 'Arctic/Longyearbyen', 'Longyearbyen'],
];

const OffsetLabel = styled('div')`
  color: ${p => p.theme.subText};
  font-weight: bold;
  display: flex;
  align-items: center;
  font-size: ${p => p.theme.fontSizeSmall};
  width: max-content;
`;

const groupedTimezones = Object.entries(groupBy(timezones, ([group]) => group));

// @ts-expect-error Should be removed once these types improve for grouped options
const timezoneOptions: SelectValue<string>[] = groupedTimezones.map(([group, zones]) => ({
  label: group,
  options: zones.map(([_, offsetLabel, value, label]) => ({
    value,
    trailingItems: <OffsetLabel>UTC {offsetLabel}</OffsetLabel>,
    label,
    textValue: `${group} ${label} ${offsetLabel}`,
  })),
}));

export {timezones, timezoneOptions};
