// Import
private import ScalarValues::Integer;
private import ISQBase::MassValue;
private import ISQBase::MassUnit;

// Parts
part def ASTRA;

part def <Motor> Nema34_BLDC{
	
}

part def <wbb> Wii_Balance_Board{
	attribute MassSupported: MassValue;
	attribute units: MassUnit;
}



// Usage
part astraSystem: ASTRA{
	part motor[2]: Motor;
	part balanceBoard: wbb;
}