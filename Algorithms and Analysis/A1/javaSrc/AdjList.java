import java.io.*;
import java.util.*;

/**
 * Adjacency list implementation for the AssociationGraph interface.
 *
 * Your task is to complete the implementation of this class.  You may add methods, but ensure your modified class compiles and runs.
 *
 * @author Jeffrey Chan, 2019.
 */
public class AdjList extends AbstractAssocGraph
{

 	/** Reference to head of list. */
     protected Node mHead;
     /** Reference to tail of list. */
     protected Node mTail;
     /** Length of list. */
     protected int mLength;

    public AdjList() {
    	 // Implement me!
         mHead = null; 
         mTail = null;
         mLength = 0;
    } // end of AdjList()


    public void addVertex(String vertLabel) {
        // Implement me!
        Node newNode = new Node(mLength, vertLabel);
             
        // If head is empty, then list is empty and head and tail references need to be initialised.
        if (mHead == null) {
            mHead = newNode;
            mTail = newNode;
        }
        // otherwise, add node to the head of list.
        else {
            newNode.setNext(mHead);
            mHead.setPrev(newNode);
            mHead = newNode;
        }
        
        mLength++;
    } // end of addVertex()


    public void addEdge(String srcLabel, String tarLabel, int weight) {
        // Implement me!
        if (weight >= mLength || weight < 0) {
            throw new IndexOutOfBoundsException("Supplied weight is invalid.");
        }

        Node newNode = new Node(weight, tarLabel);

        // index == 0
        if (mHead == null) {			
            mHead = newNode;
            mTail = newNode;
        }
        // list is not empty
        else {
            // depending on where index is, we either go forward or backward in list
         
            if (weight < Math.ceil(mLength / 2)) {
                Node currNode = mHead;
                for (int i = 0; i < weight-1; ++i) {
                    currNode = currNode.getNext();
                }

                // nextNode is the one being shift up
                Node nextNode = currNode.getNext();
                nextNode.setPrev(newNode);
                newNode.setNext(nextNode);
                newNode.setPrev(currNode);
                currNode.setNext(newNode);            
            }
            else {
                Node currNode = mTail;
                for (int i = mLength-1; i > weight; --i) {
                    currNode = currNode.getPrev();
                }

                Node prevNode = currNode.getPrev();
                prevNode.setNext(newNode);
                newNode.setPrev(prevNode);
                newNode.setNext(currNode);
                currNode.setPrev(newNode);                            
            }
        }

        mLength += 1;
    } // end of addEdge()


    public int getEdgeWeight(String srcLabel, String tarLabel) {
		    // Implement me!
            // update return value
            Node currNode = mHead;
            currNode.getValue();
            Node nextNode = mTail;
            nextNode.getValue();
         if (mHead == null) 
            {
            return EDGE_NOT_EXIST;
            }

            if(currNode.getValue() == nextNode.getValue())
            {
            return currNode.getValue();
            }
    return 100000;
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


    protected class Node {
    	
        /** Stored value of node. */
        private int mValue;
        /** Reference to next node. */
        private Node mNext;
        /** Reference to previous node. */
        private Node mPrev;

        public Node(int weight, String tarlabel ) {
            mValue = weight;
            mNext = null;
            mPrev = null;
        }

        public int getValue() {
            return mValue;
        }


        public Node getNext() {
            return mNext;
        }
        
        
        public Node getPrev() {
            return mPrev;
        }


        public void setValue(int value) {
            mValue = value;
        }


        public void setNext(Node next) {
            mNext = next;
        }
        
        public void setPrev(Node prev) {
            mPrev = prev;
        }

	}
    
} // end of class AdjList
