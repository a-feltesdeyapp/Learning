package OvenDefs{
    private import SI::*;
    private import ScalarValues::Integer;

    part def Rack;
    part def Drawer{
        part extraRack: Rack;
    }
    part def HeatingElement{
        attribute temperature: TemperatureDifferenceUnit;
    }
    part def Oven{
        attribute wattage: PowerUnit;
        attribute slotCount: Integer;
        part rack: Rack;
        part drawer: Drawer;
        part heatingElement: HeatingElement;
    }
}

package OccurrenceUsage_2{
    private import CookingDefs::*;
    private import OvenDefs::*;

    occurrence testCooking: Cooking{
        timeslice preheat: Preheat;
        timeslice cook: Cook;
        timeslice cool: Cool;

        ref part newOven: Oven;
    }
}