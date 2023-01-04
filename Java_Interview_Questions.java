# What are ACID Properties
# what is CAP Theorem
# What is time complexity of quick sort
# what is time complexity of HashMap put
# what is time complexity of LinkedList add
# what is time complexity of LinkedList get(i)
# what is time complexity of ArrayList get(i)
# what does Binary search work
# Marker Interface
## A marker interface can be defined as the interface having no data member and member functions. In simpler terms, an empty interface is called the Marker interface
## E.g. Serializable, Cloneable


# Object class is the top parent class in Java. Java.lang.Object class has few methods
# protected Object clone() throws CloneNotSupportedException
#Creates and returns a copy of this object

# public boolean equals(Object obj)
#Indicates whether some other object is "equal to" this one

# protected void finalize() throws Throwable
# Called by the garbage collecor an on object when garbagecollection determines that there are no more refwrences to the object


# public final Class getClass() : returns the run time class of an object
# public int hashCode(): returns a hash code value of the object
#public String toString(): returns a string representation of the object

#public final void notify()
#public final void notifyAll()
# public final void wait()
# public final void wait(long timeout)
# public final void wait(long timeout, int nanos)

# make a class immutablle
# declare a class final so it cant be extended
# make the fields private so that no direct access is allowed
# don't provide setter methods
# make all mutable fields final so that their value can be assigned only once
# initialize all fields via constuctor performing a deep copy
# perform cloning of objects in the getter methods to return a copy rather than returning the actual object reference
# A variable declared with the final keyword is a final variable used to prevent from overriding and overloading
# if we create a method as final then it can not ve overridden by subclasses
# a package in java is used to group related classes or it is a collection of related classes
# packages are used to avoid name conflicts between classes and it allows to write better maintaneble code

# different types of packages
# built in and user define

# An abstract class is a restricted class where we cannot create objects of the class
# to access the members of the abstract class, it must be inherited toa subclass where we can then access the members
# of the abstract class through the object of the subclass
# An abstract class can have both regular methods and abstract methods




