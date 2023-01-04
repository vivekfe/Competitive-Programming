// Using volatile is yet another way (like synnchronized, atomic wrapper) of making a class thread safe. Thread safe means that a method or class instance
// can be used by multiple threads at the same time without any problem.

class SharedObj {
// changes made to SharedVar in one thread may not immedidetly be reflected in anther thread
  static int sharedVar = 6;
}
// each of the threads are working on sharedVar. If two threads run on different processors each thread may have its own local copy of variable.
// note that writing of normal variables without any synchronization

// volatility vs synchronized : before we move on let's take a look at two important features of locks and synchronization.
//   1. Mutual exclusion: it means that only one thread or process can execute a block of code at a time
//   2. Visibility: it means changes made by one thread to shared data are visible to other threads
  
  
//  Java's synchronized keyword guarantees both mutual exclusion and visibility. if we make the block of threads that modify the value of the shared variable synchronized 
//   only one thread can enter the block and changes made by it will be reflected in the main memory. All other threads trying to enter the block at the same time will be blocked
//   and put to sleep.
    
//   In some cases we desire visibility and not atomicity. The use of synchronized in such situation is an overkill and may cause scalability problems. Here volatile 
//   comes to the rescue. Volatile variables have the visibility features of synchronized but not the atomicity features. 
    
//   The values of the volatile variable will be never cached and all writes and reads will be done to and from the main memory.
    
