private import ScalarValues::Integer;
private import SI::PowerUnit;

part def Oven {
	attribute rackCount: Integer;
	attribute wattage: PowerUnit;
}

// Adding 2 lower and upper racks.
part def Rack;

part testOven: Oven{
	part lowerRack: Rack;
	part upperRack: Rack;
}

// Feature-member relationship: X is composed of Y
// Black-diamond head
	// Racks are features of the oven
	
// Can also create part usages without definitions.
	// Bad habit to get into. Loses reuse and standardization across multiple parts
part testOven2 {
	part lowerRack2;
	part upperRack2;
}