import java.io.*;
import java.util.*;

import org.graalvm.compiler.hotspot.stubs.OutOfBoundsExceptionStub;


/**
 * Adjacency matrix implementation for the AssociationGraph interface.
 *
 * Your task is to complete the implementation of this class.  You may add methods, but ensure your modified class compiles and runs.
 *
 * @author Jeffrey Chan, 2019.
 */
public class AdjMatrix extends AbstractAssocGraph
{
    protected HashMap<String, String, Integer> adjM;


	/**
	 * Contructs empty graph.
	 */
    public AdjMatrix() {
        // Implement me!
        mVert = null;
        mWeight = 0;
        adjM = new HashMap<String, Integer>();
    } // end of AdjMatrix()


    public void addVertex(String vertLabel) {
        // Implement me!
        adjM.add(vertLabel);
    } // end of addVertex()


    public void addEdge(String srcLabel, String tarLabel, int weight) throws IndexOutOfBoundsException{
        // Implement me!
        if(adjM.containsValue(srcLabel)){
            adjM.add(srcLabel + " " + tarLabel, weight);
        }
        else{
            throw new IndexOutOfBoundsException("Vertex Doesn't Exist");
        }

    } // end of addEdge()


	public int getEdgeWeight(String srcLabel, String tarLabel) {
		// Implement me!
        if(adjM.containsValue(srcLabel + " " + tarLabel)){
            return weight;
        }
        else{
		// update return value
        return EDGE_NOT_EXIST; 
        }
	} // end of existEdge()


	public void updateWeightEdge(String srcLabel, String tarLabel, int weight) {
        // Implement me!
    } // end of updateWeightEdge()


    public void removeVertex(String vertLabel) {
        // Implement me!
    } // end of removeVertex()


	public List<MyPair> inNearestNeighbours(int k, String vertLabel) {
        List<MyPair> neighbours = new ArrayList<MyPair>();

        // Implement me!

        return neighbours;
    } // end of inNearestNeighbours()


    public List<MyPair> outNearestNeighbours(int k, String vertLabel) {
        List<MyPair> neighbours = new ArrayList<MyPair>();

        // Implement me!

        return neighbours;
    } // end of outNearestNeighbours()


    public void printVertices(PrintWriter os) {
        // Implement me!
    } // end of printVertices()


    public void printEdges(PrintWriter os) {
        // Implement me!
    } // end of printEdges()

} // end of class AdjMatrix
