package ConstraintDefinition{
    private import SI::*;

    part def Oven{
        attribute temperature: TemperatureDifferenceUnit;
        // TemperatureDifferenceUnit is defined in SI Library
    }

    constraint def CookingTemperature{
        testOven: Oven;
        testOven.temperature == 533 [K]
        // Square bracket notes that unit is defined in library used for attribute
    }
}