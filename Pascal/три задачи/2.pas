var 
  i, j, b:integer;
  mas:array[0..9] of integer;
  
begin
  for i:=0 to 9 do mas[i]:=Random(5);
  println(mas);
  for i:=0 to 9 do begin
  for j:=i+1 to 8 do begin
  if mas[j] = mas[i] then b:=1;
  end;
  end;
  if b=1 then print('yes') else print('no');
  end.