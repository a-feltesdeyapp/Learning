part def Oven;
part def HeatingElement{
	attribute temperature;
}

part testOven: Oven {
	part heatingElement: HeatingElement;
}

