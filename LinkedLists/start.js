// let obj1={a:true}
// let obj2=obj1


// console.log("1",obj1)
// console.log("2",obj2)

//10--->5--->16

// let myLinkedList={
//   head:{
//     value:10,
//     next: {
//      value:5,
//      next:{
//       value:16,
//       next:null
//      }        
//     }    
//   }

// }

class LinkedList{
  constructor(value){
    this.head={
      value:value,
      next:null
    }
    this.tail=this.head
    this.length=1
  }
printListArray(){
  const arr=[]
  let currentNode=this.head
  while(currentNode!==null){
    arr.push(currentNode.value);
    currentNode=currentNode.next
  }
  return arr

}



  append(value){
    const newNode={
      value:value,
      next:null
    }
    this.tail.next=newNode;
    this.tail=newNode
    this.length++

  

  }
  prepend(value){
    const newNode={
      value:value,
      next:null
    }
   newNode.next=this.head;
   this.head=newNode
   this.length++
  }

  insert(index,value){
    if(index>=this.length){
      return this.append(value)
    }
    



  }


}

//checks &tests
const myLinkedList=new LinkedList(10)
myLinkedList.append(5)
myLinkedList.append(16)
myLinkedList.prepend(44)
myLinkedList.insert(20,39) //add to the end since index is out of bound
console.log(myLinkedList.printListArray())