> Process, kurā programmatūra vai aparatūra tiek dekonstrēta, lai no tās iegūt papildis informāciju (bieži saistītu ar arhitektūru un implementāciju).


> `man ascii`

## [[Rīki]]
* [[GEF]]
* [[Ghidra]]
* [[Binary Ninja]]
* [[radare2]]
* [[IDA]]
* [[DnSPy]]
* [[binwalk]]
## Uzdevumu risināšanas algoritms
1. Analīze
2. Rīku izvēle
3. Dekompilācija, ja nepieciešams
4. Darbplūsmas, loģikas un mainīgo analīze
5. Modifikācija, ja nepieciešams
6. Rezultātu iegūšana

```mermaid
graph TB
	A(Identificēt faila formātu) --> B(Dekompilēt programmu)
	A --> C(Palaist failu)
	A --> D(Izgūst tekstu, strings)
	A --> E(Izpētīt faila header)
	C --> F(Identificēt darbplūsmas)
	F --> G(Identificēt interesējošās atmiņas adreses)
	B --> H(Uzbrukuma virsma)
	G --> H
	D --> H
	E --> H
	H --> I(Modificēt elementus, atmiņas adreses u.c)
```


