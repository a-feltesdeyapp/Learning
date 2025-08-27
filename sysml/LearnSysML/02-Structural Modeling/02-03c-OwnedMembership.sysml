private import SI::PowerUnit;
    private import ScalarValues::Integer;

    part def Oven {
        attribute wattage: PowerUnit;
        attribute rackCount: Integer;

        part def Rack;  // This time, we are defining the rack as belonging to the Oven
    }

    part testOven: Oven{
        part racks[2]: Rack;
    }