const
  N = 30;

var
  A: array[1..N] of integer; 
  i, x, y: integer; 
  s: real;

begin
  for i := 1 to N do A[i] := Random(40) + 160; 
  for i := 1 to N do if A[i] < 180 then A[i] := -1;
  x := 200;
  for i := 1 to N do 
  begin
    if A[i] <> -1 then begin
      if A[i] < x then begin
        x := A[i];
      end;
    end;
  end;
  write(x);
end.