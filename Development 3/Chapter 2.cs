// BA 27
class Program {
  public static void Main() {
    Tuple<bool, int, int, int> a = Tuple.Create(true, 0, 5, 40);

    while ( a.Item1 ) {
      a = Tuple.Create(a.Item1, a.Item2 + a.Item3, a.Item3, a.Item4);
      if (a.Item2 >= a.Item4) {
        a = Tuple.Create(false, a.Item2, a.Item3, a.Item4);
      }
    }
  }
}