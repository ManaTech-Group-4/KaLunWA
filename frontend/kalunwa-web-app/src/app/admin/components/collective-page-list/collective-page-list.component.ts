import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { of } from 'rxjs';
import { map } from 'rxjs/operators';
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

  constructor(private service:CollectivePagesService,private ref: ChangeDetectorRef) { }


    ngOnInit(): void {
      this.service.getProjectList().subscribe(
        (data) => {
          this.projects = data;
          this.displayList = this.projects;
        }
      );
      this.service.getEventList().subscribe(
        (data) => {
          this.events = data;
        }
      );
      this.service.getNewsList().subscribe(
        (data) => {
          this.news = data;
        }
      );
      this.service.getAnnouncementList().subscribe(
        (data) => {
          this.announcement = data;
        }
      );
        console.log(this.projects);
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
    console.log(this.currentPage, this.lastPage);
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


