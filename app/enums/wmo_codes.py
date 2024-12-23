from enum import Enum


class WMOCode(Enum):
    CLEAR_SKY = (0, "Clear sky")
    MAINLY_CLEAR = (1, "Mainly clear")
    PARTLY_CLOUDY = (2, "Partly cloudy")
    OVERCAST = (3, "Overcast")
    FOG = (45, "Fog")
    RIME_FOG = (48, "Depositing rime fog")
    DRIZZLE_LIGHT = (51, "Drizzle: Light intensity")
    DRIZZLE_MODERATE = (53, "Drizzle: Moderate intensity")
    DRIZZLE_DENSE = (55, "Drizzle: Dense intensity")
    FREEZING_DRIZZLE_LIGHT = (56, "Freezing drizzle: Light intensity")
    FREEZING_DRIZZLE_DENSE = (57, "Freezing drizzle: Dense intensity")
    RAIN_SLIGHT = (61, "Rain: Slight intensity")
    RAIN_MODERATE = (63, "Rain: Moderate intensity")
    RAIN_HEAVY = (65, "Rain: Heavy intensity")
    FREEZING_RAIN_LIGHT = (66, "Freezing rain: Light intensity")
    FREEZING_RAIN_HEAVY = (67, "Freezing rain: Heavy intensity")
    SNOW_SLIGHT = (71, "Snow fall: Slight intensity")
    SNOW_MODERATE = (73, "Snow fall: Moderate intensity")
    SNOW_HEAVY = (75, "Snow fall: Heavy intensity")
    SNOW_GRAINS = (77, "Snow grains")
    RAIN_SHOWERS_SLIGHT = (80, "Rain showers: Slight intensity")
    RAIN_SHOWERS_MODERATE = (81, "Rain showers: Moderate intensity")
    RAIN_SHOWERS_VIOLENT = (82, "Rain showers: Violent intensity")
    SNOW_SHOWERS_SLIGHT = (85, "Snow showers: Slight intensity")
    SNOW_SHOWERS_HEAVY = (86, "Snow showers: Heavy intensity")
    THUNDERSTORM_SLIGHT = (95, "Thunderstorm: Slight or moderate")
    THUNDERSTORM_HAIL_SLIGHT = (96, "Thunderstorm with hail: Slight intensity")
    THUNDERSTORM_HAIL_HEAVY = (99, "Thunderstorm with hail: Heavy intensity")