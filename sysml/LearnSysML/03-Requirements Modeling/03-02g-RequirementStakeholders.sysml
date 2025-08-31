package RequirementStakeholders{
    private import RevisitConstraints::RevisedConstraintDef::*;

    part def ProductDesign;
    
    requirement def <Req01> CookingTemperatureRequirement{
        doc
        /* Assuming the oven is on
        * The oven shall heat up to at least 533 [K]
        */
        subject testOven: Oven;
        stakeholder productDesign: ProductDesign;
        assume constraint OvenIsOn;
        require constraint CookingTemperature;
    }
}