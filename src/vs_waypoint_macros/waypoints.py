"""Predefined waypoint categories and waypoints for Vintage Story."""

from vs_waypoint_macros.models import Category, Icon, KeyCode, Waypoint

# Categories
CATEGORY_POI = Category("POI", KeyCode.NUM0, Icon.STAR1, "#FFD700")
CATEGORY_METALS = Category("Metals", KeyCode.NUM1, Icon.PICK, "#CD7F32")
CATEGORY_MINERALS = Category("Minerals", KeyCode.NUM2, Icon.ROCKS, "#4A6670")
CATEGORY_GRAINS = Category("Grains", KeyCode.NUM3, Icon.GRAIN, "#DAA520")
CATEGORY_CROPS = Category("Crops", KeyCode.NUM4, Icon.TURNIP, "#228B22")
CATEGORY_MUSHROOMS = Category("Mushrooms", KeyCode.NUM5, Icon.MUSHROOM, "#8B4513")
CATEGORY_BERRIES = Category("Berries", KeyCode.NUM6, Icon.BERRIES, "#DC143C")
CATEGORY_TREES_WARM = Category("Trees (Warm)", KeyCode.NUM7, Icon.TREE, "#228B22")
CATEGORY_TREES_COLD = Category("Trees (Cold)", KeyCode.NUM8, Icon.TREE2, "#2F4F4F")
CATEGORY_RESOURCES = Category("Resources", KeyCode.NUM9, Icon.ROCKS, "#708090")

# All predefined waypoints
WAYPOINTS: list[Waypoint] = [
    # POI
    Waypoint(CATEGORY_POI, "POI", KeyCode.NUM0),
    Waypoint(CATEGORY_POI, "Home", KeyCode.NUM1, "#4169E1", Icon.HOME),
    Waypoint(CATEGORY_POI, "Outpost", KeyCode.NUM2, "#FFA500", Icon.GEAR),
    Waypoint(CATEGORY_POI, "Ruin", KeyCode.NUM3, "#8B8682", Icon.RUINS),
    Waypoint(CATEGORY_POI, "Temporal Instability", KeyCode.NUM4, "#9400D3", Icon.SPIRAL),
    Waypoint(CATEGORY_POI, "Cave", KeyCode.NUM5, "#4A4A4A", Icon.CAVE),
    Waypoint(CATEGORY_POI, "Trader", KeyCode.NUM6, "#DAA520", Icon.TRADER),
    Waypoint(CATEGORY_POI, "Lore", KeyCode.NUM7, "#8B4513", Icon.VESSEL),
    # Metals
    Waypoint(CATEGORY_METALS, "Metal", KeyCode.NUM0),
    Waypoint(CATEGORY_METALS, "Copper", KeyCode.NUM1, "#B87333"),
    Waypoint(CATEGORY_METALS, "Tin", KeyCode.NUM2, "#D3D4D5"),
    Waypoint(CATEGORY_METALS, "Lead", KeyCode.NUM3, "#535353"),
    Waypoint(CATEGORY_METALS, "Gold", KeyCode.NUM4, "#FFD700"),
    Waypoint(CATEGORY_METALS, "Silver", KeyCode.NUM5, "#C0C0C0"),
    Waypoint(CATEGORY_METALS, "Zinc", KeyCode.NUM6, "#BAC4CB"),
    Waypoint(CATEGORY_METALS, "Bismuth", KeyCode.NUM7, "#E8B4D8"),
    Waypoint(CATEGORY_METALS, "Iron", KeyCode.NUM8, "#434343"),
    Waypoint(CATEGORY_METALS, "Meteoric Iron", KeyCode.NUM9, "#5C4033"),
    # Minerals
    Waypoint(CATEGORY_MINERALS, "Mineral", KeyCode.NUM0),
    Waypoint(CATEGORY_MINERALS, "Quartz", KeyCode.NUM1, "#E6E6E6"),
    Waypoint(CATEGORY_MINERALS, "Bituminous coal", KeyCode.NUM2, "#2C2C2C"),
    Waypoint(CATEGORY_MINERALS, "Anthracite", KeyCode.NUM3, "#1A1A1A"),
    Waypoint(CATEGORY_MINERALS, "Alum", KeyCode.NUM4, "#F5F5F5"),
    Waypoint(CATEGORY_MINERALS, "Borax", KeyCode.NUM5, "#FFFEF0"),
    Waypoint(CATEGORY_MINERALS, "Cinnabar", KeyCode.NUM6, "#E34234"),
    Waypoint(CATEGORY_MINERALS, "Halite", KeyCode.NUM7, "#FFE4E1"),
    Waypoint(CATEGORY_MINERALS, "Sylvite", KeyCode.NUM8, "#FFB6C1"),
    Waypoint(CATEGORY_MINERALS, "Lapis lazuli", KeyCode.NUM9, "#26619C"),
    Waypoint(CATEGORY_MINERALS, "Olivine", KeyCode.DIV, "#9AB973"),
    Waypoint(CATEGORY_MINERALS, "Lignite", KeyCode.MULT, "#5C4033"),
    Waypoint(CATEGORY_MINERALS, "Saltpeter", KeyCode.SUB, "#D3D3D3"),
    Waypoint(CATEGORY_MINERALS, "Sulfur", KeyCode.ADD, "#FFFF00"),
    # Grains
    Waypoint(CATEGORY_GRAINS, "Grain", KeyCode.NUM0),
    Waypoint(CATEGORY_GRAINS, "Flax", KeyCode.NUM1, "#6495ED"),
    Waypoint(CATEGORY_GRAINS, "Spelt", KeyCode.NUM2, "#D4A84B"),
    Waypoint(CATEGORY_GRAINS, "Rice", KeyCode.NUM3, "#FFFEF0"),
    Waypoint(CATEGORY_GRAINS, "Rye", KeyCode.NUM4, "#C4A35A"),
    Waypoint(CATEGORY_GRAINS, "Sunflower", KeyCode.NUM5, "#FFD700"),
    Waypoint(CATEGORY_GRAINS, "Amaranth", KeyCode.NUM6, "#9B2335"),
    Waypoint(CATEGORY_GRAINS, "Cassava", KeyCode.NUM7, "#F5DEB3"),
    # Crops
    Waypoint(CATEGORY_CROPS, "Crop", KeyCode.NUM0),
    Waypoint(CATEGORY_CROPS, "Carrot", KeyCode.NUM1, "#ED9121"),
    Waypoint(CATEGORY_CROPS, "Onion", KeyCode.NUM2, "#C9A86C"),
    Waypoint(CATEGORY_CROPS, "Turnip", KeyCode.NUM3, "#9B59B6"),
    Waypoint(CATEGORY_CROPS, "Parsnip", KeyCode.NUM4, "#F5F5DC"),
    Waypoint(CATEGORY_CROPS, "Soybean", KeyCode.NUM5, "#A4C639"),
    Waypoint(CATEGORY_CROPS, "Peanut", KeyCode.NUM6, "#C19A6B"),
    Waypoint(CATEGORY_CROPS, "Pineapple", KeyCode.NUM7, "#FFE135"),
    # Mushrooms
    Waypoint(CATEGORY_MUSHROOMS, "Mushroom", KeyCode.NUM0),
    Waypoint(CATEGORY_MUSHROOMS, "Edible (ground)", KeyCode.NUM1, "#D2B48C"),
    Waypoint(CATEGORY_MUSHROOMS, "Edible (tree)", KeyCode.NUM2, "#C4A776"),
    Waypoint(CATEGORY_MUSHROOMS, "Poisonous (ground)", KeyCode.NUM3, "#DC143C"),
    Waypoint(CATEGORY_MUSHROOMS, "Poisonous (tree)", KeyCode.NUM4, "#B22222"),
    # Berries
    Waypoint(CATEGORY_BERRIES, "Berry", KeyCode.NUM0),
    Waypoint(CATEGORY_BERRIES, "Blueberry", KeyCode.NUM1, "#4F86F7"),
    Waypoint(CATEGORY_BERRIES, "Cranberry", KeyCode.NUM2, "#9F000F"),
    Waypoint(CATEGORY_BERRIES, "Red currant", KeyCode.NUM3, "#E34234"),
    Waypoint(CATEGORY_BERRIES, "Black currant", KeyCode.NUM4, "#2E1A47"),
    Waypoint(CATEGORY_BERRIES, "White currant", KeyCode.NUM5, "#F5F5DC"),
    # Trees (Warm)
    Waypoint(CATEGORY_TREES_WARM, "Tree (Warm)", KeyCode.NUM0),
    Waypoint(CATEGORY_TREES_WARM, "Acacia", KeyCode.NUM1, "#C19A6B"),
    Waypoint(CATEGORY_TREES_WARM, "Kapok", KeyCode.NUM2, "#8FBC8F"),
    Waypoint(CATEGORY_TREES_WARM, "Purpleheart", KeyCode.NUM3, "#69359C"),
    Waypoint(CATEGORY_TREES_WARM, "Ebony", KeyCode.NUM4, "#3D3635"),
    Waypoint(CATEGORY_TREES_WARM, "Green Bamboo", KeyCode.NUM5, "#4F7942"),
    Waypoint(CATEGORY_TREES_WARM, "Brown Bamboo", KeyCode.NUM6, "#8B7355"),
    Waypoint(CATEGORY_TREES_WARM, "Bald Cypress", KeyCode.NUM7, "#6B8E23"),
    Waypoint(CATEGORY_TREES_WARM, "Redwood", KeyCode.NUM8, "#A45A52"),
    # Trees (Cold)
    Waypoint(CATEGORY_TREES_COLD, "Tree (Cold)", KeyCode.NUM0),
    Waypoint(CATEGORY_TREES_COLD, "Oak", KeyCode.NUM1, "#806517"),
    Waypoint(CATEGORY_TREES_COLD, "Maple", KeyCode.NUM2, "#C04000"),
    Waypoint(CATEGORY_TREES_COLD, "Walnut", KeyCode.NUM3, "#5C4033"),
    Waypoint(CATEGORY_TREES_COLD, "Birch", KeyCode.NUM4, "#F5F5DC"),
    Waypoint(CATEGORY_TREES_COLD, "Larch", KeyCode.NUM5, "#4A5D23"),
    Waypoint(CATEGORY_TREES_COLD, "Pine", KeyCode.NUM6, "#01796F"),
    Waypoint(CATEGORY_TREES_COLD, "Mediterranean Cypress", KeyCode.NUM7, "#4A6741"),
    Waypoint(CATEGORY_TREES_COLD, "Crimson King Maple", KeyCode.NUM8, "#722F37"),
    # Resources
    Waypoint(CATEGORY_RESOURCES, "Resource", KeyCode.NUM0),
    Waypoint(CATEGORY_RESOURCES, "Blue Clay", KeyCode.NUM1, "#5F7C8A", Icon.ROCKS),
    Waypoint(CATEGORY_RESOURCES, "Red Clay", KeyCode.NUM2, "#C04000", Icon.ROCKS),
    Waypoint(CATEGORY_RESOURCES, "Fire Clay", KeyCode.NUM3, "#CD5C5C", Icon.ROCKS),
    Waypoint(CATEGORY_RESOURCES, "Peat", KeyCode.NUM4, "#3C280D", Icon.ROCKS),
    Waypoint(CATEGORY_RESOURCES, "Medium Fertility Dirt", KeyCode.NUM5, "#8B4513", Icon.ROCKS),
    Waypoint(CATEGORY_RESOURCES, "High Fertility Dirt", KeyCode.NUM6, "#3D2817", Icon.ROCKS),
    Waypoint(CATEGORY_RESOURCES, "Cattails", KeyCode.NUM7, "#6B8E23", Icon.GRAIN),
    Waypoint(CATEGORY_RESOURCES, "Tule", KeyCode.NUM8, "#808000", Icon.GRAIN),
    Waypoint(CATEGORY_RESOURCES, "Resin", KeyCode.NUM9, "#FFBF00", Icon.TREE),
]

ALL_CATEGORIES = [
    CATEGORY_POI,
    CATEGORY_METALS,
    CATEGORY_MINERALS,
    CATEGORY_GRAINS,
    CATEGORY_CROPS,
    CATEGORY_MUSHROOMS,
    CATEGORY_BERRIES,
    CATEGORY_TREES_WARM,
    CATEGORY_TREES_COLD,
    CATEGORY_RESOURCES,
]
