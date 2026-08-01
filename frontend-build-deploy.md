
Lets learn about 
```yml
defaults:
  run:
    working-directory: ./frontend
```
> `defaults.run.working-directory` affects only run: steps. <strong>It does NOT affect uses: actions</strong>.

### Issue 1:

When I kept the run.working directory to ./frontend and used `uses: actions/upload-artifact@v4`
the artifact is created it in the pulumi-crator/dist

and when i try to pull the artifact in the deploy step
Why didn't upload find dist?

Because the upload action searched here:

> /home/runner/work/pulumi-crator/pulumi-crator/dist

It never searched inside frontend, because working-directory does not affect uses: actions.