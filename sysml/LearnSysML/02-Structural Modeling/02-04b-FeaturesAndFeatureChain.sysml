private import SI::*;

part def HeatingElement {
    attribute temperature: TemperatureDifferenceUnit;    // Value Feature
}

part def Oven{
    part heatingElement: HeatingElement;    // Part feature 
}

// To demo the use of features, use a script to model an action
action def setupTest{
in testOven: Oven;
assign testOven.heatingElement.temperature := 500 [K];   // This is when you finally get to assign actual numbers to things
}