package StakeholderConcern{
    private import SI::*;
    private import RevisitConstraints::RevisedConstraintDef::*;

    concern def SafetyConcern{  // Concern is defined as such
        subject oven: Oven;
        part def Person;

        stakeholder productDesigner: Person;    // This is the stakeholder raising concern

        attribute surfaceTemperature: TemperatureDifferenceUnit;

        // Concern expressed with `require` and documents a constraint that can be defined
        // and modeled further in req specification
        require constraint {
            doc /* The oven's external surface temperature shall not exceed 300 [K]*/
        }
    }
}