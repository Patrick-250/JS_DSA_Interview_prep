
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

    //add a new node at the end of a linkedlist...  o of one time complexity
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

//remove the last employee... o of n time complexity
pop(){
    if(!this.head){
        return undefined
    }
    let current=this.head //current last node... this to be returned
    let newTail=current //new last node

    while(current.next){
        newTail=current
        current=current.next
    }
    this.tail=newTail
    this.tail.next=null
    this.length--

    if(this.length===0){
        this.head=null
        this.tail=null

    }
return current
}

//remove the first element in the list

shift(){
    if(!this.head){
        return undefined
    }
   
    let currentFirst=this.head
    this.head=this.head.next
    currentFirst.next=null
    this.length--
    if(this.length===0){
        this.tail=null
    }
    return currentFirst

}

//add a new node at the start of a linkedlist
unshift(value){
    const newNode=new Node(value)
    if(!this.head){
        this.head=newNode
        this.tail=newNode  
    }
    else{
        newNode.next=this.head
        this.head=newNode
    }
    this.length++
    return this

}

//add a new node at a specific index position
insert(index,value){

}




}


const myTeam=new employees("Rumanzi")
myTeam.push("Engineer 1")
myTeam.push("Engineer 2")
myTeam.push("engineer3")
myTeam.unshift("this goes at start of the list")


// myTeam.pop()
// console.log( myTeam.pop())



console.log(myTeam)