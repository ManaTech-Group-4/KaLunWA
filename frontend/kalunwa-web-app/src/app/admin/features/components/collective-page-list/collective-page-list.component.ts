import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { MatSnackBar } from '@angular/material/snack-bar';
import { ConfirmDialog } from '../../dialogs/confirm-dialog/confirm-dialog';
import { CollectivePageModel } from '../../model/collective-page-model';
import { CollectivePagesService } from '../../service/collective-pages.service';


@Component({
  selector: 'app-collective-page-list',
  templateUrl: './collective-page-list.component.html',
  styleUrls: ['./collective-page-list.component.scss']
})
export class CollectivePageListComponent implements OnInit {


  projects: CollectivePageModel[];
  announcement: CollectivePageModel[];
  events: CollectivePageModel[];
  news: CollectivePageModel[];
  displayList: CollectivePageModel[];
  activePage:number = 1;
  currentPage = 0;
  lastPage = 4;
  selected="project";

  constructor(private service: CollectivePagesService,
    private ref: ChangeDetectorRef,
    private dialog: MatDialog,
    private snackBar: MatSnackBar) { }


    ngOnInit(): void {
      this.getEvent();
      this.getNews();
      this.getAnnouncement();
      this.getProject();
    }

  getProject(){
    const projSub = this.service.getProjectList().subscribe(
      (data) => {
        this.projects = data;
        this.displayList = this.projects;
        projSub.unsubscribe();
      }
    );
  }

  getEvent(){
    const eventSub = this.service.getEventList().subscribe(
      (data) => {
        this.events = data;
        this.displayList = this.events;
        eventSub.unsubscribe();
      }
    );
  }
  getNews(){
    const newsSub = this.service.getNewsList().subscribe(
      (data) => {
        this.news = data;
        this.displayList = this.news;
        newsSub.unsubscribe();
      }
    );
  }
  getAnnouncement(){
    const annSub = this.service.getAnnouncementList().subscribe(
      (data) => {
        this.announcement = data;
        this.displayList = this.announcement;
        annSub.unsubscribe();
      }
    );
  }



  detectIfChanges(){
    this.ref.detectChanges();
  }

  updateDisplay(newPage:number){
    this.currentPage += (8*(newPage-this.activePage));
    if(this.currentPage < 0)
      this.currentPage = 0;

    this.lastPage = this.currentPage + 8;
    if(this.lastPage > this.displayList.length)
      this.lastPage = this.displayList.length;


    this.activePage = newPage;
    this.ref.detectChanges();
  }

  deleteItem(id:number, name:string){
    const dialogRef = this.dialog.open(ConfirmDialog, {
      width: '250px',
      data: `Do you like to delete the ${this.selected} ${name}`,
    });



    const dialogSubscribe = dialogRef.afterClosed().subscribe(result => {
      if(result){
        if(this.selected == "project"){
          const deleteSub = this.service.deleteProject(id).subscribe(
            res =>{
              this.getProject();
              this.updateDisplay(this.activePage);
              this.snackBar.open(`Successfully deleted ${this.selected}`, `Close`, {duration: 5000});
              deleteSub.unsubscribe();
            },
            err =>{
              console.log(err);
            }
          );
        }
        else if(this.selected == "event"){
          const deleteSub = this.service.deleteEvent(id).subscribe(
            res =>{
              this.getEvent();
              this.updateDisplay(this.activePage);
              this.snackBar.open(`Successfully deleted ${this.selected}`, `Close`, {duration: 5000});
              deleteSub.unsubscribe();
            },
            err =>{
              console.log(err);
            }
          );
          }
        else if(this.selected == "news"){
          const deleteSub = this.service.deleteNews(id).subscribe(
            res =>{
              this.getNews();
              this.updateDisplay(this.activePage);
              this.snackBar.open(`Successfully deleted ${this.selected}`, `Close`, {duration: 5000});
              deleteSub.unsubscribe();
            },
            err =>{
              console.log(err);
            }
          );
        }
        else if(this.selected == "announcement"){
          const deleteSub = this.service.deleteAnnouncement(id).subscribe(
            res =>{
              this.getAnnouncement();
              this.updateDisplay(this.activePage);
              this.snackBar.open(`Successfully deleted ${this.selected}`, `Close`, {duration: 5000});
              deleteSub.unsubscribe();
            },
            err =>{
              console.log(err);
            }
          );
        }
      }
    dialogSubscribe.unsubscribe();
    });
  }


  changeCollection(collection:string){
    this.selected=collection;
    if(collection == "project")
      this.displayList = this.projects;
    else if(collection == "event")
      this.displayList = this.events;
    else if(collection == "news")
      this.displayList = this.news;
    else if(collection == "announcement")
      this.displayList = this.announcement;


    this.updateDisplay(1);
  }

}


