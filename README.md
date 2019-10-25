## Kart Race Test

This software emulates a kart race using data in the following format. 

```
Hora                               Piloto             Nº Volta   Tempo Volta       Velocidade média da volta
23:49:08.277      038 – F.MASSA                           1             1:02.852                        44,275
23:49:10.858      033 – R.BARRICHELLO                     1             1:04.352                        43,243
23:49:11.075      002 – K.RAIKKONEN                       1             1:04.108                        43,408
23:49:12.667      023 – M.WEBBER                          1             1:04.414                        43,202
23:49:30.976      015 – F.ALONSO                          1             1:18.456                        35,47
```

---

## Getting Started

You must have `Python 3.6` or higher to run the project. No external libs are needed for this project.

Clone the repository

`git clone https://github.com/giovana-morais/kart_test.git`

and then run the project

`python main.py <log_file.txt>`


## Sample Output


```
Final podium:
	1 -- (038) F.MASSA -- Total laps: 4. total time: 00:04:11.578000
	2 -- (002) K.RAIKKONEN -- Total laps: 4. total time: 00:04:15.153000
	3 -- (033) R.BARRICHELLO -- Total laps: 4. total time: 00:04:16.080000
	4 -- (023) M.WEBBER -- Total laps: 4. total time: 00:04:17.722000
	5 -- (015) F.ALONSO -- Total laps: 4. total time: 00:04:54.221000
	6 -- (011) S.VETTEL -- Total laps: 3. total time: 00:06:27.276000
Pilots' best laps:
	F.MASSA best lap was lap 2, which time was 00:01:02.769000
	R.BARRICHELLO best lap was lap 2, which time was 00:01:03.716000
	K.RAIKKONEN best lap was lap 3, which time was 00:01:03.076000
	M.WEBBER best lap was lap 3, which time was 00:01:04.216000
	F.ALONSO best lap was lap 1, which time was 00:01:07.011000
	S.VETTEL best lap was lap 2, which time was 00:01:18.097000
Pilot's average speed:
	F.MASSA average speed was 44.246 km/h
	R.BARRICHELLO average speed was 43.468 km/h
	K.RAIKKONEN average speed was 43.627 km/h
	M.WEBBER average speed was 43.191 km/h
	F.ALONSO average speed was 38.066 km/h
	S.VETTEL average speed was 25.746 km/h
```
