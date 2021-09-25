import java.util.*;

class singly_linkedlistmain{
    public static void main(String[] args){
        SinglyLL<Integer> ll = new SinglyLL<Integer>();
        ll.addAtBegining(10);
        ll.addAtBegining(20);
        ll.addAtEnd(30);
        ll.addAtEnd(60);

        ll.show_ll();

        System.out.println("The element at index 2 :"+ll.get(2).data);

        ll.removeAtBegining();

        ll.show_ll();

        ll.addAtBegining(70);

        ArrayList<Integer> ls = ll.toArray();

        System.out.println("Converted to array ------>");
        for(Integer i : ls){
            System.out.print(i+" ");
        }
    }
}
class Node<T>{
    T data;
    Node<T> Next;

    Node(T d){
        data=d;
        Next=null;
    }
}
class SinglyLL<T>{
    Node<T> head;

    void addAtBegining(T x){
        Node<T> temp= new Node<T>(x);
        if(head==null){
            head=temp;
        }
        else{
            temp.Next=head;
            head=temp;
        }
    }
    void addAtEnd(T x){
        Node<T> temp = new Node<T>(x);
        if(head==null){
            head=temp;
        }
        else{
            Node traverse = head;
            while(traverse.Next !=null){
                traverse = traverse.Next;
            }

            traverse.Next=temp;

        }
    }
    void removeAtBegining(){
        if(head==null){
            System.out.println("Empty linked list ");

        }
        else{
            head=head.Next;
        }
    }
    void removeAtEnd(){
        if(head == null){
            System.out.println("Empty linked list ");
        }
        else{
            Node traverse = head;
            while(traverse.Next !=null){
                traverse = traverse.Next;
            }
            traverse = null;
        }
    }
     Node<T> get(int i){
        Node traverse = head;
        if(head==null){
            System.out.println("Empty linked list ");
            return head;
        }
        else {
            for(int x=0; x<=i && traverse!=null ; x++){
                traverse = traverse.Next;
            }


            return traverse;
        }
    }
    ArrayList<T> toArray(){
        ArrayList<T> arr = new ArrayList<T>();
        Node<T> traverse = head;

        while(traverse!=null){
            arr.add(traverse.data);
            traverse= traverse.Next;
        }
        return arr;
    }
    void show_ll(){
        Node<T> traverse = head;

        System.out.print("Head --> ");
        while (traverse!=null){
            System.out.print(traverse.data+" --> ");
            traverse = traverse.Next;
        }
        System.out.println("NULL");
    }
}
