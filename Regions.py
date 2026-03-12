from typing import Dict, List, NamedTuple

from .Names import RegionName

class AstronautilusRegionData(NamedTuple):
    connecting_regions: List[str] = []


region_data_table: Dict[str, AstronautilusRegionData] = {
    "Menu": AstronautilusRegionData([RegionName.forsaken_city]),

    RegionName.World: AstronautilusRegionData([RegionName.world_1, RegionName.world_2, RegionName.world_3, RegionName.world_4, RegionName.world_5]),

    RegionName.world_1:     AstronautilusRegionData([RegionName.shop_1]),
    RegionName.world_2:     AstronautilusRegionData([RegionName.shop_2]),
    RegionName.world_3:     AstronautilusRegionData([RegionName.shop_3]),
    RegionName.world_4:     AstronautilusRegionData([RegionName.shop_4]),
    RegionName.world_5:     AstronautilusRegionData([RegionName.shop_5]),

    RegionName.forsaken_city: AstronautilusRegionData([RegionName.intro_islands, RegionName.granny_island, RegionName.highway_island, RegionName.ne_feathers_island, RegionName.se_house_island, RegionName.badeline_tower_upper, RegionName.badeline_island]),

    RegionName.intro_islands:        AstronautilusRegionData([RegionName.granny_island]),
    RegionName.granny_island:        AstronautilusRegionData([RegionName.highway_island, RegionName.nw_girders_island, RegionName.badeline_tower_lower, RegionName.se_house_island, RegionName.cassette_entrance_1, RegionName.cassette_entrance_2, RegionName.cassette_entrance_4]),
    RegionName.highway_island:       AstronautilusRegionData([RegionName.granny_island, RegionName.ne_feathers_island, RegionName.nw_girders_island, RegionName.cassette_entrance_3, RegionName.cassette_entrance_6]),
    RegionName.nw_girders_island:    AstronautilusRegionData([RegionName.highway_island]),
    RegionName.ne_feathers_island:   AstronautilusRegionData([RegionName.se_house_island, RegionName.highway_island, RegionName.badeline_tower_lower, RegionName.badeline_tower_upper, RegionName.cassette_entrance_7, RegionName.cassette_entrance_8]),
    RegionName.se_house_island:      AstronautilusRegionData([RegionName.ne_feathers_island, RegionName.granny_island, RegionName.badeline_tower_lower, RegionName.cassette_entrance_5]),
    RegionName.badeline_tower_lower: AstronautilusRegionData([RegionName.se_house_island, RegionName.ne_feathers_island, RegionName.granny_island, RegionName.badeline_tower_upper]),
    RegionName.badeline_tower_upper: AstronautilusRegionData([RegionName.badeline_island, RegionName.badeline_tower_lower, RegionName.se_house_island, RegionName.ne_feathers_island, RegionName.granny_island, RegionName.cassette_entrance_9]),
    RegionName.badeline_island:      AstronautilusRegionData([RegionName.badeline_tower_upper, RegionName.granny_island, RegionName.highway_island, RegionName.cassette_entrance_10]),

    RegionName.cassette_1:  AstronautilusRegionData([]),
    RegionName.cassette_2:  AstronautilusRegionData([]),
    RegionName.cassette_3:  AstronautilusRegionData([]),
    RegionName.cassette_4:  AstronautilusRegionData([]),
    RegionName.cassette_5:  AstronautilusRegionData([]),
    RegionName.cassette_6:  AstronautilusRegionData([]),
    RegionName.cassette_7:  AstronautilusRegionData([]),
    RegionName.cassette_8:  AstronautilusRegionData([]),
    RegionName.cassette_9:  AstronautilusRegionData([]),
    RegionName.cassette_10: AstronautilusRegionData([]),

    RegionName.cassette_entrance_1:  AstronautilusRegionData([]),
    RegionName.cassette_entrance_2:  AstronautilusRegionData([]),
    RegionName.cassette_entrance_3:  AstronautilusRegionData([]),
    RegionName.cassette_entrance_4:  AstronautilusRegionData([]),
    RegionName.cassette_entrance_5:  AstronautilusRegionData([]),
    RegionName.cassette_entrance_6:  AstronautilusRegionData([]),
    RegionName.cassette_entrance_7:  AstronautilusRegionData([]),
    RegionName.cassette_entrance_8:  AstronautilusRegionData([]),
    RegionName.cassette_entrance_9:  AstronautilusRegionData([]),
    RegionName.cassette_entrance_10: AstronautilusRegionData([]),
}

cassette_entrance_regions: List[str] = [
    RegionName.cassette_entrance_1,
    RegionName.cassette_entrance_2,
    RegionName.cassette_entrance_3,
    RegionName.cassette_entrance_4,
    RegionName.cassette_entrance_5,
    RegionName.cassette_entrance_6,
    RegionName.cassette_entrance_7,
    RegionName.cassette_entrance_8,
    RegionName.cassette_entrance_9,
    RegionName.cassette_entrance_10,
]

cassette_regions: List[str] = [
    RegionName.cassette_1,
    RegionName.cassette_2,
    RegionName.cassette_3,
    RegionName.cassette_4,
    RegionName.cassette_5,
    RegionName.cassette_6,
    RegionName.cassette_7,
    RegionName.cassette_8,
    RegionName.cassette_9,
    RegionName.cassette_10,
]

