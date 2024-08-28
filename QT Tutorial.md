## QT Tutorial

- Qt is a cross-platform framework that is usually used as a graphical toolkit.

- Qt has a collection of modules, including:

  - `QtCore`, provides containers, thread management, event management, etc.
  - `QtGui`&`QtWidgets`, provides a lot of graphical components to design app.
  - `QtNetwork`, that provides classes for dealing with network communications.
  - `QtWebkit`, enable the use of web pages and web app.
  - `QtSQL`, SQL RDBM abstraction layer extensible with own drivers.
  - `QtXML`, for simple XML parsing and DOM
  - `QtXmlPatterns`, for XXSLT, XPath, XQuery and Schema validation.

- **Qt Creator**, 是一个 C++ IDE，它非常适合编写 Qt 程序，提供了文档浏览器和设计器。

- 每个 Qt object 都有很多 **properties**，与一般的 field 一样可以 set/get，更重要的是可以被订阅 (subscribe)。订阅后 property 的更新会出发 events。

- **Qt 的类型系统**广泛使用了继承。

  - ![Beginner-Class-Hierarchy.jpg](/Users/chenchen/Documents/books-notes/assets/Beginner-Class-Hierarchy.jpg)
  - `QObject` is the most basic class in Qt，它提供了如下基础能力：
    - Object name: 设置对象名称，用于搜索
    - Parenting system
    - Signals and slots
    - Event management
  -  `QWidget` is able to respond to events and use parenting system and signals and slots mechanism.
    - `QWidget` contains most properties that are used to describe a window/widget. like position, size, mouse cursor, tooltips etc.

- **Parenting system** 用于表示 widgets 在图形上的包含关系，composition 而非 inheritance。

  - Child widgets automatically appear inside the parent widget.

  - When an object is destroyed, all of its children are destroyed too.

    ```c++
    QWidget window;
    window.setFixedSize(100, 50);
    QPushButton *button = new QPushButton("Hello", &window);
    button->setGeometry(10, 10, 80, 30);
    window.show();
    ```

- **Subclassing QWidget**

  - Qt GUI 编程常用的设计模式是，create a class that is used to display a window, and implement all the widgets that are contained in this window as properties of this class.

  - 比如，我们可以定义一个主窗口 `Window` class，然后在其 constructor 中实现其内部 UI。

    ```c++
    class Window: public QWidget {
      QPushButton *m_button;
    public:
      explicit Window(QWidget *parent=nullptr): QWidget(parent) {
        // set size of the window
        setFixedSize(100, 50);
        // create and position the button
        m_button = new QPushButton("Hello", this);
        m_button->setGeometry(10, 10, 80, 30);
      }
    }
    ```

- **Signals and slots**

  - UI 组件的用户交互的实现一般都采用 observer pattern，Qt 中对 observer pattern 做了一层抽象，定义了 signal/slot 机制。

  - Observer pattern 本质是一种控制反转，也称为 who-is-boss。同情况下是，函数调用数据，而在 observer pattern 中是 数据调用函数。

  - Signal 是事件消息，Slot 是处理消息的响应函数。

  - 每个 `QWidget` 都有一些 signals，比如 `QPushbutton` 有 `clicked`, `pressed`, `released` 等 signals。

  - Slot 可以是任何 (无返回值) 方法或函数，比如 `QApplication::quit`, `QWidget::setEnabled`。

  - 实现 Signal-Slot 的链接，需要用到 `QObject::connect` 方法和两个 macro: `SIGNAL` 和 `SLOT`。

    - ```c++
      auto* manager = new MediaProgressManager();
      auto* progress = new QProgressBar(widows);
      QObject::connect(manager, SIGNAL(tick(int)), progress, SLOT(setValue(int)));
      ```

    - 需要注意的是，QT 中 signal 也是方法而非单纯的数据，毕竟单纯的数据是无法进行函数调用的。SIGNAL/SLOT macro 后跟的是函数签名。signal 和 slot 函数的签名需要是相同的，一般用来指定消息数据。

  - 一个 signal 可以连接多个 slots；多个 signal 可以连接同一个 slot；一个 signal 可以连接另一个 signal (signal relaying)。

---

Each object has a storage duration that determines its lifetime, which is the time during program execution for which the object exists, has storage, has a constant address, and retains its last-stored value. Objects must not be referenced outside their lifetime.

Local variables have automatic storage duration, meaning that they exist until execution leaves the block in which they're defined.

When used in a function declaration or definition, `*` acts as part of a pointer declarator indicating that the parameter is a pointer to an object or function of a specific type.

Objects, functions, macros, and other identifiers have scope that delimitsthe contiguous region where they can be accessed. C has four types of scope: file, block, function prototype, function.

The scope of an object or function identifier is determined by where it is declared. If the declaration is outside any block or parameter list, the identifier has file scope, meaning the scope is entire text file in which it appears as well as files included after that point.

If the declaration appears inside a block or within the list of parameters, it has block scope, meaning that the identifier it declares is accessible only within the block.

the identifiers for a and b have block scope and can be used to refer to only these variables within the code block in the main function in which they're defined.

If the declaration appears within the list of parameter declarations in a functio prototype, the identifier has function prototype scope, which terminates at the end of the function declarator.

Function scope is the area between the opening `{` of a function definition and its closing `}`.

A label name is the only kind of identifier that has function scope. Labels are identifiers followed by a colon and identify a statement in a function to which control may be transferred.

Scopes can be nested, with inner and outer scopes.

Four example, you can have a block scope inside another block scope, and every block scope is defined within a file scope. The inner scope has access to the outer scope.

Objects have a storage duration that determines their lifetime. Altogether, four storage durations are available: automatic, static, thread, and allocated.

you have seen that objects of automatic storage duration are declared within a block or as a function parameter.

the lifetime of these objects begins when the block in which they're declared begins execution, and ends when execution of the block ends.

If the block is entered recursively, a new object is created each time, each with its own storage.

Scope and lifetime are entirely different concepts. 

scope applies to identifiers, whereas lifetime applies to objects.

the scope of an identifier is the code region where the object denoted by the identifier can be accessed by its name.

the lifetime of an object is the time period for which the object exists.

Object declared in file scope have static storage duration. The lifetime of these objects is the entire execution of the program, and their stored value is initialized prior to program startup.

you can also declare a variable within a block scope to have static storage duration by using the storage class specifier `static`.

Of course, to run programs, and stop them, and otherwise tell the os which program to run, there need to be some APIs that you can use to communicate your desires to the OS.

we will talk about these APIs throughout this book; indeed, they are the major way in which most users interact with operating systems.

you might also notice that the ability to run multiple programs at once raises all sorts of new questions.

Now let's consider memory. the model of physical memory presented by modern machines is very simple. Memory is just an array of bytes; to read memory, one just specify an address to be able to access the data stored there; to write memory, one must also specify the data to be written to the given address.

memory is accessed all the time when a program is running. a program keeps all of its data structures in memory, and accesses them through various instructions, like loads, stores, or other explicit instructions that access memory in doing their work.

don't forget that each instruction of the program is in memory too; thus memory is accessed on each instruction fetch.

Let's take a look at a program that allocates some memory by calling `malloc()`. The output of this program can be found here.

The program does a couple of things. first, it allocates some memory. then it prints out the address of the memory, and then puts the number zero into the first slot of the newly allocated memory.

Again, this first result is not too interesting. The newly allocated memory is at address `0x2000`. as the program runs, it slowly updates the value and prints out the result.

Now, we again run multiple instances. we see from the example athat each running program has allocated memory at the same address, and yet each seems to be updating the value indpendently.

It is as if each runnning program has its own private memory, instead of sharing the same physical memory with other program.

Indeed, that is exactly what is happening here as the OS is virtualizing memory. Each process accesses its own private virtual address space, which the OS somehow maps onto the physical memory of the machine.

A memory reference within one running program does not affect the address space of other processes; as far as the running program is concerned, it has physical memory all to itself.

The reality, however, is that physical memory is a shared resource, managed by the os. exactly how all of this is accomplished is also the subject of the first part of this book on the topic of virtualization.

the problems of concurrency are no longer limited just to the os itself. indeed, modern multi-threaded programs exhibit the same problems. Let us demonstrate with an example of a multi-threaded program.

Although you might not understnad this example fully at the moment, the basic idea is simple. the main program creates two threads using `Pthread_create`. You can think of a thread as a function running within the same memory space as other functions, with more than one of them active at a time.

----

So now you have some idea of what an OS actually does: it takes physical resources, such as a CPU, memory, or disk, and virtualizes them.

It handles tough and tricky issues related to concurrency. And it stores files persistently, thus making them safe over the long-term.

Given that we want to build such a system, we want to have some goals in mind to help focus our design and implementation and make trade-offs as necessary; finding the right set of trade-offs is a key to building systems.

One of the most basic goals is to build up some abstractions in order to make the system convenient and easy to use.

Abstractions are fundamental to everything we do in computer science. Abstraction makes it possible to write a large program by dividing it into small and understandable pieces, to write such a program in a high-level language like C without thinking about assembly, to write code in assembly without thinking about logic gates, and to build a processor out of gates without thinking too much about transistors.

Abstraction is so fundamental that sometimes we forget its importance, but we don't here; thus, in each section, we will discuss some of the major abstractions that have developed over time, giving you a way to think about pieces of the OS.

One goal in designing and implementing an operating system is to provide high performance; another way to say this is our goal is to minimize the overheads of the OS.

Virtualization and makeing the ssytem easy to use are well worth it, but not at any cost; thus, we must strive to provide virtualization and other OS feattures without excessive overheads.

These overheads arise in a number of forms: extra time and extra space. We'll seek solutions that minimize one or the other or both, if possible. Perfection, however, is not always attainable, something we will learn to notice and tolerate.

Another goal will be to proivde protection between applications, as well as between the os and apps. because we wish to allow many programs to run at the same time, we want to make sure that the malicious or accidental bad behavior of one does not harm others;

we certainly don't want an app to be able to harm the os itself.

protection is at the heart of one of the main principles underlying an operating system, which is that of isolation; isolating processes from oen another is the key to protection and thus underlies much of waht an OS must do.

The operating system must also run non-stop; when it fails, all applications running on the system fail as well.

Because of this dependence, operating systems often strive to provide a high degree of reliability.

as operating systems grow evermore complex (sometimes containing millions of lines of code), building a reliable operating system is quite a challenge, and indeed, much of the on-going research in the field focuses on this exact problem.

Other goals make sense: energy-efficiency is important in our increasingly green world; security against malicious applications is critical, especially in these highly-networked time; mobility is increasingly important as OSes are run on smaller and smaller devices.

Depending on how the system is used, the OS will have different goals and thus likely be implemented in at least slightly different ways.

In this chapter, we discuss one of the most fundamental abstractions that the OS provides to users: the process.

the definition of a process, informally, is quite simple: it is a running program.

the program itself is a lifeless thing: it just sits there on the disk, a bunch of instructions, waiting to spring into action.

It is the operating system that takes these bytes and gets them running, transforming the program into something useful.

It turns out that one often wants to run more than one program at once, for example, consider your desktop or laptop where you might like to run a web browser, mail program, a game, a music player, and so forth.

in fact, a typical system may be seemingly running tens or even hundreds of processes at the same time. Doing so makes the system easy to use, as one never need be concerned with whether a CPU is available; one simply runs programs. Hence our challenge:

The OS creates this illusion by virtualizing the CPU. By running one process, then stopping it and running another, and so forth, the OS can promote the illusion that many virtual CPUs exist when in fact there is only one CPU.

this basic technique, known as time sharing of the CPU, allows users to run as many concurrent processes as they would like; the potential cost is performance, as each will run more slowly if the CPU must be shared.

To implement virtualization of the CPU, and to implement it well, the OS will need both some low-level machinery and some high-level intelligence.

we call the low-level machinery mechanisms; mechanisms are low-level methods or protocols that implement a needed piece of functionality.

for example, we will learn later how to implement a context switch, which gives the OS the ability to stop running one program and start running another on a given CPU; this time-sharing mechanism is employed by all modern OSes.

On top of these mechanisms resides some of the intelligence in the OS, in the form of policies. Policies are algorithms for making some kind of decision within the OS.

for example, given a number of possible programs to run on a CPU, which program should the OS run?

A scheduling policy in the OS will make this decision, like using historical information, workload knowledge and performance metrics to make its decision.

Time sharing is a basic technique used by an OS to share a resource. By allowing the resource to be used for a little while by one entity, and then a little while by another, and so forth, the resource in question can be shared by many.

the counterpart of time sharing is space sharing, where a resource is divided among those who wish to use it.

one mystery that we should unmask a bit is how program are transformed into process. specificaly, how does the os get a program up and running? how does process creation actually work?

the first thing that the os must do to run a program is to load its code and any static data into memory, into the address space of the process.

programs initially reside on disk in some kind of executable format; thus the process of loading a program and static data into memory requires the OS to read those bytes from disk and place them in memory somewhere.

In early os, the loading process is done eagerly, i.e. all at one before running the program; modern os perform the process lazily, ie. by loading pieces of code or data only as they are needed during program execution.

To truly understand how lazy loading of pieces of code and ata works, you will have to understand more about the machinery of paging and swapping, topics we'll cover when we discuss the virtualization of memory.

For now, just remember that before running, the os clearly must do some work to get the important porgram bits from disk into memory.

let's look at one more example before getting to some questions. In this example, the process just issues IO requests. We specify that IO take 5 time units to complete with the flag `-L`.

as you can see, the program just issues three IOs, when each IO is issued, the process moves to a BLOCKED state, and while the device is busy servicing the IO, the CPU is idle.

To handle the completion of the IO, one more CPU action takes place. Note that a single instruction to handle IO initiation and completion is not particularly realistic, but just used here for simplicity.

as you can see, the trace took 21 clock ticks to run, but the cpu was busy less than 30% of the time. The IO device,, on the other hand, was quite busy. In general, we'd like to keep all the device busy, as that is a better use of resources.

In this interlude, we discuss process creation in unix systems. Unix presents one of the most intriguing ways to create a new process with a pair of system calls: `fork` and `exec`. A third routine, `wait` can be used by a process wishing to wait for a process it has created to complete.

we now present these interfaces in more detail, with a few simple examples to motivate us. Ans thus, our problem.

What interfaces should the OS present for process creation and control? How should these interfaces be designed to enable powerful functionality, ease of use, and high performance?

In this interlude, we discuss process creation in UNIX systems. UNIX presents one of the most intriguing ways to create a new process with a pair of system calls: `fork()` and `exec()`.

A third routine, `wait()`, can be used by a process wishing to wait for a process it has created to complete. We now present ehese interfaces in more detail, with a few simple examples to motivate us. And thus, our problem:

> What interfaces should the OS present for process creation and control?
>
> How should these interfaces be designed to enable powerful functionality, ease of use, and high performance?

The `fork()` system call is used to create a new process. However, be forewarned: it is certainly the strangest routine you will ever call.

More specifically, you have a running program whose code looks like what you see.Let us understand what happened in more detail. 

when it first started running, the process prints out a help world message; include in that message is its process identifier, also known as a PID. The process has a PID of 29; the pid is used to name the process if one wants to do something with the process, such as stop it from running. so far, so good.

Now the interesting part begins. the process calls the `fork()` system call, which the OS provides as a way to create a new process.

The odd part: the process that is created is an exact copy of the calling process.

That means that to the OS, it now looks like there are two copies of the program `p1` running, and both are about to return from the `fork()` system call.

In this example, the child process calls `execvp()` in order to run the program `wc`, which is the world counting program. In fact, it runs `wc` on the source file, thus telling us how many lines, words, and bytes are found in the file.

The shell is just a user program. It shows you a prompt and then waits for you to type something into it.

you then type a command into itl in most cases, the shell then figures out where in the file system the executable resides, calls `fork()` to create a new child process to run the command, calls some variant of `exec()` to run the command, and then waits for the command to complete by calling `wait()`.

when the child completes, the shell returns from `wait()` and prints out a prompt again, ready for your next command.

the separation of `fork()` and `exec()` allows the shell to do a whole bunch of useful things rather easily. For example:

```
>> wc p3.c > newfile.txt
```

In the example above, the output of the program `wc` is redirected into the output file `newfile.txt`.

The way the shell accomplishes this task is quite simple: when the child is created, before calling `exec()`, the shell closes standard output and opens the file `Newfie.txt`. By doing so, any output from the soon-to-be-running program `wc` are sent to the file instead of the screen.

Figure 5.4 shows a program that does exactly this. The reason this redirection works is due to an assumption about how the os manages file descrptors.

Specifically, unix start looking for free file descriptors at zero. In this case, `STDOUT_FILENO` will be the first available one and thus get assigned when `open()` is called.



