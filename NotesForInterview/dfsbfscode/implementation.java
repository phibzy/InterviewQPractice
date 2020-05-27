public class Graph {
   private HashMap<Integer, Node> nodeLookup = new HashMap<Integer, Node>();
   public static class Node {
      private int id;
      LinkedList<Node> adjacent = new LinkedList<Node>();
      private Node(int id) {
         this.id = id;
      }
   }

   private Node getNode(int id) {
      return this.nodeLookup(id);
   }
   
   public void addEdge(int source, int destination) {
      Node s = getNode(source);
      Node d = getNode(destination);
      s.adjacent.add(d);
   }


   // Alternative: Iterative solution you use a stack
   public boolean hasPathDFS(int source, int destination) {
      Node s = getNode(source);
      Node d = getNode(destination);
      HashSet<Integer> visited = new HashSet<Integer>();
      return hasPathDFS(s, d, visited);
   }

   public boolean hasPathDFS(Node source, Node destination, HashSet<Integer> visited) {
      if (visited.contains(source.id)) {
         return false;
      }

      visited.add(source.id);

      if (source == destination) {
         return true;
      }

      for (Node neighbour : source.adjacent) {
         if hasPathDFS(neighbour, destination, visited) {
            return true;
         }
      }

      return false;

   }

   public boolean hasPathBFS(Node source, Node destination) {
      HashSet<Int> visited = new HashSet<Int>();
      Queue<Node> q = new Queue<Node>;

      q.enqueue(source);

      while (!q.isEmpty()) {
         Node next = q.dequeue();
         if (visited.contains(q)) continue;
         if (next == source) {
            return true;
         }
         visited.add(source);

         for (Node n : next.adjacent) {
            q.enqueue(n);   
         }
      }

      return false;

   }










}
