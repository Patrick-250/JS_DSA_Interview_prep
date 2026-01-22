
class Node{
    constructor(value){
        this.value=value;
        this.next=null

    }
}


class employees{
    constructor(value){
        const newNode=new Node(value)
        this.head=newNode
        this.tail=this.head
        this.length=1
    }

    //add a new node at the end of a linkedlist
push(value){
const newNode=new Node(value)
if(!this.head){
    this.head=newNode
    this.tail=newNode
}
else{
    this.tail.next=newNode
    this.tail=newNode

}
this.length++
return this
}

//add a new node at the start of a linkedlist
unshift(value){

}

//add a new node at a specific index position
insert(index,value){

}




}


const myTeam=new employees("Rumanzi")
myTeam.push("Engineer 1")
myTeam.push("Engineer 2")



console.log(myTeam)