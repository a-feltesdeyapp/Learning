private import SI::PowerUnit;
private import ScalarValues::Integer;

part def Oven{
	attribute wattage: PowerUnit;
	attribute rackCount: Integer;
}

part def Rack;

// define parts as array of usages within same part definition
part testOven: Oven{
	part racks[2]: Rack;	// Array of racks, with number of array, 2
}