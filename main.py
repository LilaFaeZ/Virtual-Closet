from website import create_app

app = create_app()

if __name__ == '__main__': #only if we run this file, are we going to execute this line
    app.run(debug=True)  #every time we make a change to our python code, it will 
    #automatically re run our python server