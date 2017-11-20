function show_create_thread_form(){
    d3.select("div#start-create-thread-form").classed("hidden",true)
    d3.select("div#in-create-thread-form").classed("hidden",false)
}

function done_create_thread_form(){
    d3.select("div#start-create-thread-form").classed("hidden",false)
    d3.select("div#in-create-thread-form").classed("hidden",true)
}

