package ConstraintWithoutDefinition{
    private import RevisitConstraints::RevisedConstraintDef::*;
    private import SI::K;

    requirement def <Req01> CookingTemperatureRequirement{
        doc
        /* Assuming the oven is on
        * The oven shall heat up to at least 533 K.
        */
        subject testOven: Oven;
        assume constraint { testOven.isOn == true }
        require constraint { testOven.temperature == 533 [K] }
    }
}