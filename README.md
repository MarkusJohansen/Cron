# Cron

My cron jobs for repetetive automated tasks.

## What is it?

Cron jobs are scheduled jobs. It is a great solution for tasks you need to do regularly. This solution allows me to run cron-jobs on github actions, while ensuring that GitHub doesnt deactivate the workflow. Repositories on github with no activity for 60 day will get their scheduled workflows deactivated. I am solving this by using a cron job (😳) that commits to the repository once a month, ensuring that my workflows are "kept alive".

## Jobs

### Pinger
The pinger application just sends a simple HTTP get request to urls in a defined list. I use this to keep my supabase databases alive for projects that i dont visit regularly.
