package RevisitRequirementDefinition{
    private import RevisitConstraints::RevisedConstraintDef::*;

    requirement def <Req01> CookingTemperatureRequirement {
        doc
        /* Assuming the oven is on, 
        * The oven shall heat up to at least 533 K.
        */
        subject testOven: Oven;
        assume constraint OvenIsOn;
        require constraint CookingTemperature;
        // KEY WORD: `require`
        
    }
}