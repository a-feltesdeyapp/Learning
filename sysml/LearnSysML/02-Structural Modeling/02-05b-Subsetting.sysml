part def Rack{
    attribute depth;
    attribute width;
}

part def Oven{
    part racks: Rack[2]; // Array of 2 racks
    part topRack subsets racks; // subset racks to make top and bottom
    part bottomRack :> racks;
}