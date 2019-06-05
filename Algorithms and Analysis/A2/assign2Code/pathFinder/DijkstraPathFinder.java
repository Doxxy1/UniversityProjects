package pathFinder;

import map.Coordinate;
import map.PathMap;

import java.util.*;

public class DijkstraPathFinder implements PathFinder
{
    /* TODO: You might need to implement some attributes
    
        newMap - so we can access map over the whole class
        visited - sets row & column of coordinate to visited if we visit it
        min / max - used for getting neighbours for the coordinate
        allCells - used for comparing with Point(for neighbours)
        neighboursOf - a hashmap that contains an origin coordinate and all of its possible neighbours
        completePath - node of coordinate as a complete path, used for adding to arraylist path to return
        cells - cells explored implementation
        globals of the starting, end and waypoint cell lists
    */
    PathMap newMap;
    int minRow = 0;
    int maxRow;
    int minCol = 0;
    int maxCol;
    List<Coordinate> allCells;
    Map<Coordinate, List<Coordinate>> neighboursOf;
    int cells;
    List<Coordinate> allWaypoints;
    List<Coordinate> startingCells;
    List<Coordinate> endCells;

    public DijkstraPathFinder(PathMap map) {
        // TODO :Implement
        newMap = map;
        maxRow = map.sizeR;
        maxCol = map.sizeC;
        allCells = new ArrayList<>();
        neighboursOf = new HashMap<Coordinate, List<Coordinate>>();

        //initialies visted & add all possible cells to allCells that are impassable
        for(int row = 0; row < maxRow; row++){
            for(int col = 0; col < maxCol; col++){
                if(map.cells[row][col].getImpassable() == false){allCells.add(map.cells[row][col]);}
            }
        }

        for(int i = 0; i < maxRow; i++){
            for(int j = 0; j < maxCol; j++){
                neighboursOf.put(map.cells[i][j], getNeighbours(map.cells[i][j].getRow(), map.cells[i][j].getColumn()));
            }
        }

        allWaypoints = newMap.waypointCells;
        startingCells = newMap.originCells;
        endCells = newMap.destCells;
    } // end of DijkstraPathFinder()



    @Override
    public List<Coordinate> findPath() {
        // You can replace this with your favourite list, but note it must be a
        // list type
        List<Coordinate> path = new ArrayList<Coordinate>();

        if(allWaypoints.size() > 0){
            path = taskD(startingCells.get(0), endCells.get(0), allWaypoints);
        }
        else if(startingCells.size() > 1 || endCells.size() > 1){
            path = taskC(startingCells, endCells);
        }
        else{path = taskAB(startingCells.get(0), endCells.get(0));}

        return path;
    } // end of findPath()

    /*
        ------Class for Task A & B------
        - Used Tutorial BFS as a foundation for our Dijkstra and built upon it 
        - Used the node reprsentations in the tutorials for the base as well
        - Used an iterator to iterate through neighbours
        - Boolean representation of visited (sets x & y coordinates to true if visited)
        - Weights of node are increased based on previous node
    */
    List<Coordinate> taskAB(Coordinate start, Coordinate end){
        PriorityQueue<Coordinate> q = new PriorityQueue<Coordinate>();
        List<Coordinate> path = new ArrayList<Coordinate>();
        Node<Coordinate> node = new Node<Coordinate>(start);
        Node<Coordinate> completePath = null;
        boolean visited[][];
        visited = new boolean[maxRow][maxCol];

        start.setTerrainCost(start.getTerrainCost());
        start.setNode(node);

        q.add(start);

        while(!q.isEmpty()){
            Coordinate current = q.remove();
            Iterable<Coordinate> neigh = neighbours(current);
            Iterator<Coordinate> iter = neigh.iterator();
            Node<Coordinate> currentNewNode = current.getNode();
            if(current.getRow() == end.getRow() && current.getColumn() == end.getColumn()){
                completePath = current.getNode();
                break;
            }
            visited[current.getRow()][current.getColumn()] = true;
            cellsExplored();

            while(iter.hasNext()){
                Coordinate nextCoordinate = iter.next();
                if(!visited[nextCoordinate.getRow()][nextCoordinate.getColumn()] &&
                !q.contains(nextCoordinate)){
                    Node<Coordinate> newNode = new Node<Coordinate>(nextCoordinate);
                    currentNewNode.addPrevious(newNode);
                    nextCoordinate.setTerrainCost(current.getTerrainCost() + nextCoordinate.getTerrainCost());
                    nextCoordinate.setNode(newNode);
                    q.add(nextCoordinate);                
                }
            }
        }
      Node<Coordinate> currentNode = completePath;
      reversePath(currentNode,path);
      return path;

    }

    //reverses the path so that start is at the front.
    public void reversePath(Node<Coordinate> coord, List<Coordinate> path)
    {
       
        while(coord != null){
            path.add(coord.getCoord());
            coord = coord.getNext();
        }
        Collections.reverse(path);
       
    }


    //Returns an iterable version of a coordinates neighbours for iterator
    public Iterable<Coordinate> neighbours(Coordinate coord){
        return neighboursOf.get(coord);
    }

    /*
        TASK C IMPLEMENTATION:
        Iterates through all possible start and end cells,
        assigns the paths to a map with the index of the map as the size of the List of Coordinates, which is the path
        we then pull out the min value of the map, assign the list to the return value.

    */
    public List<Coordinate> taskC(List<Coordinate> start, List<Coordinate> end){
        List<Coordinate> actualPath = new ArrayList<>();
        Map<Integer, List<Coordinate>> path = new HashMap<>();
     
        for(int i = 0; i < start.size(); i++){
            for(int j = 0; j < end.size(); j++){
                List<Coordinate> newPath = taskAB(start.get(i), end.get(j));
                int weightofPath = newPath.size();
                path.put(weightofPath, newPath);
            }
        }

        int min = Collections.min(path.keySet());
        actualPath = path.get(min);
        return actualPath;
        
    }


    /*
        Task D:
        We built the path going from start to waypoint 1, then waypoint 1 to waypoint 2 etc etc,
        then when there is no more waypoints to traverse, we do the last waypoint to the destination
        and print that path.
        If the waypoint is only 1, we only do it once and terminate after that
        (our if statement)
    */
    public List<Coordinate> taskD(Coordinate start, Coordinate end, List<Coordinate> waypoint){
        List<Coordinate> wayPoint = new ArrayList<>();
        List<Coordinate> path = taskAB(start, waypoint.get(0));
        
        if(waypoint.size() > 1){
            for(int i = 0; i < waypoint.size() - 1; i++){
                wayPoint.addAll(taskAB(waypoint.get(i), waypoint.get(i + 1)));
            }
        }
        else{
            wayPoint.addAll(taskAB(waypoint.get(0), end));
            wayPoint.remove(waypoint.get(0));
            path.addAll(wayPoint);
            return path;
        }
        List<Coordinate> destinationPath = taskAB(waypoint.get(waypoint.size() - 1), end);
        path.addAll(wayPoint);
        path.addAll(destinationPath);
        return path;   
    }

    //returns the cost of the current path (- 1 for general java workings)
    int getCost(List<Coordinate> path){
        return path.get(path.size() -1).getTerrainCost();
    }

    @Override
    public int cellsExplored() {
        // TODO: Implement
        cells++;
        // placeholder
        return cells;
    } // end of cellsExplored()


    /*
    Gets neighbours based on the x & y axis, then iterates through allCells to find out if the
     point(x,y) equals a coordinate in allCells
    */
    public List<Coordinate> getNeighbours(int x, int y) {
        List<Point> ret = new ArrayList<>(); 
        List<Coordinate> neighbours = new ArrayList<>();
        for (int i = Math.max(x - 1, minRow); i <= Math.min(x + 1, maxRow); i++)
           for (int j = Math.max(y - 1, minCol); j <= Math.min(y + 1, maxCol); j++) {
            //neighbour of itself, and diagonal options
              if (i == x && j == y)continue;
              if( i - x == j - y ) continue;
              if(i - x == y - j)continue;
              ret.add(new Point(i, j));
           }
        for(Point point : ret){
            for(Coordinate coord : allCells){
                if(coord.getRow() == point.x && coord.getColumn() == point.y){
                    neighbours.add(coord);
                }
            }
        }


        return neighbours;
     }

     /*
        Inner point class for getting the x (row) and y (col) so its easier to loop through getting
        neighbours.
     */
     class Point{
        int x;
        int y;

        Point(int x, int y){
            this.x=x;
            this.y=y;
        }

        int getX(){
            return x;
        }
        int getY(){
            return y;
        }

    }
    /*
        Inner class, A node representation of Coordinate
    */
    public class Node<Coordinate>{
        Coordinate coord;
        Node<Coordinate> next;
        List<Node<Coordinate>> previous;

        Node(Coordinate coord){
            this.coord = coord;
            previous = new ArrayList<Node<Coordinate>>();
        }

        Coordinate getCoord(){
            return coord;
        }

        List<Node<Coordinate>> getPrevious(){
            return previous;
        }

        void addPrevious(Node<Coordinate> prev){
            prev.setNext(this);
            previous.add(prev);
        }

        void setNext(Node<Coordinate> next){
            this.next = next;
        }

        Node<Coordinate> getNext(){
            return next;
        }
    }



} // end of class DijsktraPathFinder
