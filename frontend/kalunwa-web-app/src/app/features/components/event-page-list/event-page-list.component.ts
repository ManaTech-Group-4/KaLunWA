import { AfterViewInit, ChangeDetectorRef, Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { Observable, of } from 'rxjs';
import { EventsItemsModel } from '../../models/event-items-model';
import { EventspageService } from '../../service/eventspage.service';

@Component({
  selector: 'app-event-page-list',
  templateUrl: './event-page-list.component.html',
  styleUrls: ['./event-page-list.component.scss']
})
export class EventPageListComponent implements OnInit {

  @Input()
  events = [] as EventsItemsModel[];
  constructor(private ref: ChangeDetectorRef) { }

  activePage:number = 1;
  currentPage = 0;
  lastPage = 4;

  detectIfChanges(){
    this.ref.detectChanges();
  }

  updateDisplay(newPage:number){
    if(newPage > this.activePage){
      this.currentPage += 5;
      if(this.lastPage+5 > this.events.length){
        this.lastPage = this.events.length;
        return;
      }
      else
        this.lastPage += 5;
    }
    else if(newPage < this.activePage){
      this.lastPage -= 5;
      if(this.currentPage-5 <0){
        this.currentPage = this.events.length;
        return;
      }
      else
        this.currentPage -= 5;
    }
    this.ref.detectChanges();
    this.activePage = newPage;
    let y =  document.querySelector('.event-card')?.getBoundingClientRect().top;
    window.scrollTo({top: y! + window.scrollY - 80, behavior: 'smooth'});
  }


  ngOnInit(): void {
  }


}
