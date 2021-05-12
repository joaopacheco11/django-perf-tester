## No queue, filter-last

55000 valores na tabela, indexado no index_field

```
Sort  (cost=1621.79..1649.17 rows=10951 width=62)
  Output: id, ifield1, ifield2, ifield3, bfield4, bfield5, tfield6, tfield7, index_field
  Sort Key: select_perf_tester_testmodel1.ifield2
  ->  Bitmap Heap Scan on public.select_perf_tester_testmodel1  (cost=125.16..887.05 rows=10951 width=62)
        Output: id, ifield1, ifield2, ifield3, bfield4, bfield5, tfield6, tfield7, index_field
        Recheck Cond: (select_perf_tester_testmodel1.index_field = 2)
        ->  Bitmap Index Scan on select_perf_tester_testmodel1_index_field_9f05362f  (cost=0.00..122.42 rows=10951 width=0)
            Index Cond: (select_perf_tester_testmodel1.index_field = 2)
```

55000 valores na tabela, nao indexado

```
Limit  (cost=1367.26..1367.26 rows=1 width=62)
  Output: id, ifield1, ifield2, ifield3, bfield4, bfield5, tfield6, tfield7, index_field
  ->  Sort  (cost=1367.26..1394.63 rows=10951 width=62)
        Output: id, ifield1, ifield2, ifield3, bfield4, bfield5, tfield6, tfield7, index_field
        Sort Key: select_perf_tester_testmodel1.ifield2
        ->  Seq Scan on public.select_perf_tester_testmodel1  (cost=0.00..1312.50 rows=10951 width=62)
              Output: id, ifield1, ifield2, ifield3, bfield4, bfield5, tfield6, tfield7, index_field
              Filter: (select_perf_tester_testmodel1.index_field = 2)
```

index em index_field e ifield2

```
Limit  (cost=0.29..0.66 rows=1 width=62)
  Output: id, ifield1, ifield2, ifield3, bfield4, bfield5, tfield6, tfield7, index_field
  ->  Index Scan using select_perf_tester_testmodel1_ifield2_44f24e6a on public.select_perf_tester_testmodel1  (cost=0.29..4074.74 rows=10951 width=62)
        Output: id, ifield1, ifield2, ifield3, bfield4, bfield5, tfield6, tfield7, index_field
        Filter: (select_perf_tester_testmodel1.index_field = 2)
```

index em ifield2

```
Limit  (cost=0.29..0.66 rows=1 width=62)
  Output: id, ifield1, ifield2, ifield3, bfield4, bfield5, tfield6, tfield7, index_field
  ->  Index Scan using select_perf_tester_testmodel1_ifield2_44f24e6a on public.select_perf_tester_testmodel1  (cost=0.29..4074.74 rows=10951 width=62)
        Output: id, ifield1, ifield2, ifield3, bfield4, bfield5, tfield6, tfield7, index_field
        Filter: (select_perf_tester_testmodel1.index_field = 2)
```

```print(TestModel1.objects.all().order_by('ifield2').filter(index_field=2)[:1].explain(verbose=True))```

```print(TestModel1.objects.get(id=Queue.objects.filter(index_field=2).order_by('ifield2')[:1]).explain(verbose=True))```

## no queue filter-first:

55000 Valores:
index em ifield2

```
Limit  (cost=0.29..0.66 rows=1 width=62)
  Output: id, ifield1, ifield2, ifield3, bfield4, bfield5, tfield6, tfield7, index_field
  ->  Index Scan using select_perf_tester_testmodel1_ifield2_44f24e6a on public.select_perf_tester_testmodel1  (cost=0.29..4074.70 rows=11011 width=62)
        Output: id, ifield1, ifield2, ifield3, bfield4, bfield5, tfield6, tfield7, index_field
        Filter: (select_perf_tester_testmodel1.index_field = 2)
```

index em index_field e ifield2

```
Limit  (cost=0.29..0.66 rows=1 width=62)
  Output: id, ifield1, ifield2, ifield3, bfield4, bfield5, tfield6, tfield7, index_field
  ->  Index Scan using select_perf_tester_testmodel1_ifield2_44f24e6a on public.select_perf_tester_testmodel1  (cost=0.29..4074.70 rows=11011 width=62)
        Output: id, ifield1, ifield2, ifield3, bfield4, bfield5, tfield6, tfield7, index_field
        Filter: (select_perf_tester_testmodel1.index_field = 2)
```

index em index_field

```
Limit  (cost=943.32..943.32 rows=1 width=62)
  Output: id, ifield1, ifield2, ifield3, bfield4, bfield5, tfield6, tfield7, index_field
  ->  Sort  (cost=943.32..970.85 rows=11011 width=62)
        Output: id, ifield1, ifield2, ifield3, bfield4, bfield5, tfield6, tfield7, index_field
        Sort Key: select_perf_tester_testmodel1.ifield2
        ->  Bitmap Heap Scan on public.select_perf_tester_testmodel1  (cost=125.63..888.26 rows=11011 width=62)
              Output: id, ifield1, ifield2, ifield3, bfield4, bfield5, tfield6, tfield7, index_field
              Recheck Cond: (select_perf_tester_testmodel1.index_field = 2)
              ->  Bitmap Index Scan on select_perf_tester_testmodel1_index_field_9f05362f  (cost=0.00..122.87 rows=11011 width=0)
                    Index Cond: (select_perf_tester_testmodel1.index_field = 2)
```

sem index

```
Limit  (cost=1367.56..1367.56 rows=1 width=62)
  Output: id, ifield1, ifield2, ifield3, bfield4, bfield5, tfield6, tfield7, index_field
  ->  Sort  (cost=1367.56..1395.08 rows=11011 width=62)
        Output: id, ifield1, ifield2, ifield3, bfield4, bfield5, tfield6, tfield7, index_field
        Sort Key: select_perf_tester_testmodel1.ifield2
        ->  Seq Scan on public.select_perf_tester_testmodel1  (cost=0.00..1312.50 rows=11011 width=62)
              Output: id, ifield1, ifield2, ifield3, bfield4, bfield5, tfield6, tfield7, index_field
              Filter: (select_perf_tester_testmodel1.index_field = 2)
```

## Queue

```
Index Scan using select_perf_tester_testmodel1_pkey on public.select_perf_tester_testmodel1  (cost=270.48..278.50 rows=1 width=62)
  Output: select_perf_tester_testmodel1.id, select_perf_tester_testmodel1.ifield1, select_perf_tester_testmodel1.ifield2, select_perf_tester_testmodel1.ifield3, select_perf_tester_testmodel1.bfield4, select_perf_tester_testmodel1.bfield5, select_perf_tester_testmodel1.tfield6, select_perf_tester_testmodel1.tfield7, select_perf_tester_testmodel1.index_field
  Index Cond: (select_perf_tester_testmodel1.id = $0)
  InitPlan 1 (returns $0)
    ->  Limit  (cost=270.19..270.19 rows=1 width=12)
          Output: u0.id, u0.ifield2
          ->  Sort  (cost=270.19..276.88 rows=2677 width=12)
                Output: u0.id, u0.ifield2
                Sort Key: u0.ifield2
                ->  Seq Scan on public.select_perf_tester_queue u0  (cost=0.00..256.80 rows=2677 width=12)
                      Output: u0.id, u0.ifield2
                      Filter: (u0.index_field = 2)
```