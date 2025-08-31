package RevisitConstraints{
    private import SI::*;
    private import ScalarValues::Boolean;   // had to import bool value type

    package RevisedConstraintDef{
        part def Oven{
            attribute temperature: TemperatureDifferenceUnit;
            attribute isOn: Boolean;    // added attribute of on bool
        }
        
        constraint def OvenIsOn{    // added constraint OvenIsOn with logic statement
            testOven: Oven;
            testOven.isOn == true
        }

        constraint def CookingTemperature{
            testOven: Oven;
            testOven.temperature == 533 [K]
        }
    }
        
}