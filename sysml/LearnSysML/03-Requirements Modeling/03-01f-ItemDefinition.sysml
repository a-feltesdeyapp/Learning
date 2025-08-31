package ItemDefinition{
    item def ElectricPower;

    part def Oven{
        item power: ElectricPower;
        // Electricity or gas flow through the oven but are not actually part of the oven
    }
}