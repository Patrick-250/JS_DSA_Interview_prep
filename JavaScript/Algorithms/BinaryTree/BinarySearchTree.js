class Node{
    constructor(value){
        this.left=null
        this.right=null
        this.value=value
    }
}

class BinaryTreeSearch{
    constructor(){
        this.root=null;
    }

    insert(){
        const newNode=new Node(value)
        if(this.root==null){
            this.root=newNode
        }
        else{
            let currentNode=this.root
            while(true){
                if(value<currentNode.value){
                    //go left
                    if(!currentNode.left){
                        currentNode.left=newNode
                        return this
                    }
                    


                }
            }
        }

    }

  lookup(){

  }



}

const tree=new BinaryTreeSearch()
