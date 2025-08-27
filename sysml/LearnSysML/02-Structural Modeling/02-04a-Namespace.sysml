part def Oven{
        part def Rack;
    }

    part def Drawer{
        // we have another rack that could be used in the oven
        // however, it is not stored in the oven, but rather in a separate drawer
        // to call upon the rack, we have to call it's fully qualified name
        part extraRack: Oven::Rack;
    }