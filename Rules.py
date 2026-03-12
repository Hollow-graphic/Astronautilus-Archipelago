from typing import Dict, List, Tuple, Callable

from BaseClasses import CollectionState, Region
from worlds.generic.Rules import set_rule

from . import AstronautilusWorld
from .Names import ItemName, LocationName, RegionName


def set_rules(world: AstronautilusWorld):
    world.active_logic_mapping = location_logic
    world.active_region_logic_mapping = region_logic

    for location in world.multiworld.get_locations(world.player):
        set_rule(location, lambda state, location=location: location_rule(state, world, location.name))

    # Completion condition.
    world.multiworld.completion_condition[world.player] = lambda state: goal_rule(state, world)


location_logic: Dict[str, List[List[str]]] = {
    LocationName.shop1_item1: [[ItemName.shopdiscount1]],
    LocationName.shop1_item2: [[ItemName.shopdiscount1]],
    LocationName.shop1_item3: [[ItemName.shopdiscount1]],
    LocationName.shop1_item4: [[ItemName.shopdiscount1]],
    LocationName.shop1_item5: [[ItemName.shopdiscount1]],
    LocationName.shop1_item6: [[ItemName.shopdiscount1]],
    LocationName.shop1_item7: [[ItemName.shopdiscount1]],
    LocationName.shop1_item8: [[ItemName.shopdiscount1]],

    LocationName.shop2_item1: [[ItemName.shopdiscount2]],
    LocationName.shop2_item2: [[ItemName.shopdiscount2]],
    LocationName.shop2_item3: [[ItemName.shopdiscount2]],
    LocationName.shop2_item4: [[ItemName.shopdiscount2]],
    LocationName.shop2_item5: [[ItemName.shopdiscount2]],
    LocationName.shop2_item6: [[ItemName.shopdiscount2]],
    LocationName.shop2_item7: [[ItemName.shopdiscount2]],
    LocationName.shop2_item8: [[ItemName.shopdiscount2]],

    LocationName.shop3_item1: [[ItemName.shopdiscount3]],
    LocationName.shop3_item2: [[ItemName.shopdiscount3]],
    LocationName.shop3_item3: [[ItemName.shopdiscount3]],
    LocationName.shop3_item4: [[ItemName.shopdiscount3]],
    LocationName.shop3_item5: [[ItemName.shopdiscount3]],
    LocationName.shop3_item6: [[ItemName.shopdiscount3]],
    LocationName.shop3_item7: [[ItemName.shopdiscount3]],
    LocationName.shop3_item8: [[ItemName.shopdiscount3]],

    LocationName.shop4_item1: [[ItemName.shopdiscount4]],
    LocationName.shop4_item2: [[ItemName.shopdiscount4]],
    LocationName.shop4_item3: [[ItemName.shopdiscount4]],
    LocationName.shop4_item4: [[ItemName.shopdiscount4]],
    LocationName.shop4_item5: [[ItemName.shopdiscount4]],
    LocationName.shop4_item6: [[ItemName.shopdiscount4]],
    LocationName.shop4_item7: [[ItemName.shopdiscount4]],
    LocationName.shop4_item8: [[ItemName.shopdiscount4]],

    LocationName.shop5_item1: [[ItemName.shopdiscount5]],
    LocationName.shop5_item2: [[ItemName.shopdiscount5]],
    LocationName.shop5_item3: [[ItemName.shopdiscount5]],
    LocationName.shop5_item4: [[ItemName.shopdiscount5]],
    LocationName.shop5_item5: [[ItemName.shopdiscount5]],
    LocationName.shop5_item6: [[ItemName.shopdiscount5]],
    LocationName.shop5_item7: [[ItemName.shopdiscount5]],
    LocationName.shop5_item8: [[ItemName.shopdiscount5]],
}

region_logic: Dict[Tuple[str], List[List[str]]] = {
    (RegionName.forsaken_city, RegionName.granny_island):        [[ItemName.checkpoint_2], [ItemName.checkpoint_3], [ItemName.checkpoint_4]],
    (RegionName.forsaken_city, RegionName.highway_island):       [[ItemName.checkpoint_5], [ItemName.checkpoint_6]],
    (RegionName.forsaken_city, RegionName.ne_feathers_island):   [[ItemName.checkpoint_7]],
    (RegionName.forsaken_city, RegionName.se_house_island):      [[ItemName.checkpoint_8]],
    (RegionName.forsaken_city, RegionName.badeline_tower_upper): [[ItemName.checkpoint_9]],
    (RegionName.forsaken_city, RegionName.badeline_island):      [[ItemName.checkpoint_10]],

    (RegionName.intro_islands, RegionName.granny_island): [[ItemName.ground_dash],
                                                           [ItemName.air_dash],
                                                           [ItemName.skid_jump],
                                                           [ItemName.climb]],

    (RegionName.granny_island, RegionName.highway_island): [[ItemName.air_dash, ItemName.dash_refill]],
    (RegionName.granny_island, RegionName.nw_girders_island): [[ItemName.traffic_block]],
    (RegionName.granny_island, RegionName.badeline_tower_lower): [[ItemName.air_dash, ItemName.climb, ItemName.dash_refill]],
    (RegionName.granny_island, RegionName.se_house_island): [[ItemName.air_dash, ItemName.climb, ItemName.double_dash_refill]],
    (RegionName.granny_island, RegionName.cassette_entrance_1): [[ItemName.breakables, ItemName.air_dash]],
    (RegionName.granny_island, RegionName.cassette_entrance_2): [[ItemName.breakables, ItemName.air_dash]],
    (RegionName.granny_island, RegionName.cassette_entrance_4): [[ItemName.dash_refill, ItemName.air_dash]],
    
    (RegionName.highway_island, RegionName.granny_island): [[ItemName.traffic_block], [ItemName.air_dash, ItemName.dash_refill]],
    (RegionName.highway_island, RegionName.ne_feathers_island): [[ItemName.feather]],
    (RegionName.highway_island, RegionName.nw_girders_island): [[ItemName.cannot_access]],
    
    (RegionName.nw_girders_island, RegionName.highway_island): [[ItemName.traffic_block]],
    
    (RegionName.ne_feathers_island, RegionName.highway_island): [[ItemName.feather]],
    (RegionName.ne_feathers_island, RegionName.badeline_tower_lower): [[ItemName.feather]],
    (RegionName.ne_feathers_island, RegionName.badeline_tower_upper): [[ItemName.climb, ItemName.air_dash, ItemName.feather]],
    (RegionName.ne_feathers_island, RegionName.cassette_entrance_7): [[ItemName.feather]],
    (RegionName.ne_feathers_island, RegionName.cassette_entrance_8): [[ItemName.climb]],
    
    (RegionName.se_house_island, RegionName.granny_island): [[ItemName.air_dash, ItemName.traffic_block, ItemName.double_dash_refill]],
    (RegionName.se_house_island, RegionName.badeline_tower_lower): [[ItemName.air_dash, ItemName.double_dash_refill]],
    (RegionName.se_house_island, RegionName.cassette_entrance_5): [[ItemName.climb]],
    
    (RegionName.badeline_tower_lower, RegionName.se_house_island): [[ItemName.cannot_access]],
    (RegionName.badeline_tower_lower, RegionName.ne_feathers_island): [[ItemName.air_dash, ItemName.breakables, ItemName.feather]],
    (RegionName.badeline_tower_lower, RegionName.granny_island): [[ItemName.cannot_access]],
    (RegionName.badeline_tower_lower, RegionName.badeline_tower_upper): [[ItemName.cannot_access]],
    
    (RegionName.badeline_tower_upper, RegionName.badeline_island): [[ItemName.air_dash, ItemName.climb, ItemName.double_dash_refill, ItemName.feather, ItemName.traffic_block, ItemName.breakables]],
    (RegionName.badeline_tower_upper, RegionName.se_house_island): [[ItemName.air_dash], [ItemName.ground_dash]],
    (RegionName.badeline_tower_upper, RegionName.ne_feathers_island): [[ItemName.air_dash], [ItemName.ground_dash]],
    (RegionName.badeline_tower_upper, RegionName.granny_island): [[ItemName.dash_refill]],
    
    (RegionName.badeline_island, RegionName.badeline_tower_upper): [[ItemName.air_dash], [ItemName.ground_dash]],
}

def location_rule(state: CollectionState, world: AstronautilusWorld, loc: str) -> bool:
    if loc not in world.active_logic_mapping:
        return True

    for possible_access in world.active_logic_mapping[loc]:
        if state.has_all(possible_access, world.player):
            return True

    return False

def region_connection_rule(state: CollectionState, world: AstronautilusWorld, region_connection: Tuple[str]) -> bool:
    if region_connection not in world.active_region_logic_mapping:
        return True

    for possible_access in world.active_region_logic_mapping[region_connection]:
        if state.has_all(possible_access, world.player):
            return True

    return False

def goal_rule(state: CollectionState, world: AstronautilusWorld) -> bool:
    if not state.has(ItemName.strawberry, world.player, world.strawberries_required):
        return False

    goal_region: Region = world.multiworld.get_region(RegionName.badeline_island, world.player)
    return state.can_reach(goal_region)

def connect_region(world: AstronautilusWorld, region: Region, dest_regions: List[str]):
    rules: Dict[str, Callable[[CollectionState], bool]] = {}

    for dest_region in dest_regions:
        region_connection: Tuple[str] = (region.name, dest_region)
        rules[dest_region] = lambda state, region_connection=region_connection: region_connection_rule(state, world, region_connection)

    region.add_exits(dest_regions, rules)
