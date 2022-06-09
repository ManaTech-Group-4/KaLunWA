import { Component, EventEmitter, Input, OnChanges, OnInit, Output } from '@angular/core';
import { Observable, of } from 'rxjs';

@Component({
  selector: 'app-app-pagination',
  templateUrl: './app-pagination.component.html',
  styleUrls: ['./app-pagination.component.scss']
})
export class AppPaginationComponent implements OnChanges {

  constructor() { }

  @Input() totalRecords = 0;
  @Input() recordsPerPage = 0;

  @Output() onPageChange: EventEmitter<number> = new EventEmitter();

  public pages: number [] = [];
  public aheadPages: number [] = [];
  public behindPages: number [] = [];
  activePage: number;

  ngOnChanges(): any {
    this.aheadPages = [];
    this.behindPages = [];
    const pageCount = this.getPageCount();
    this.pages = this.getArrayOfPage(pageCount);
    this.activePage = 1;
    this.onPageChange.emit(1);
  }

  private  getPageCount(): number {
    let totalPage = 0;

    if (this.totalRecords > 0 && this.recordsPerPage > 0) {
      const pageCount = this.totalRecords / this.recordsPerPage;
      const roundedPageCount = Math.floor(pageCount);

      totalPage = roundedPageCount < pageCount ? roundedPageCount + 1 : roundedPageCount;
    }
    for(let i =1; i<=5 && i<=totalPage; i++)
      this.behindPages.push(i);
    return totalPage;
  }

  private getArrayOfPage(pageCount: number): number [] {
    const pageArray = [];

    if (pageCount > 0) {
        for(let i = 1 ; i <= pageCount ; i++) {
          pageArray.push(i);
        }
    }

    return pageArray;
  }

  onClickPage(pageNumber: number): void {
      if (pageNumber >= 1 && pageNumber <= this.pages.length) {
          this.activePage = pageNumber;
          this.onPageChange.emit(this.activePage);
          this.aheadPages = [];
          this.behindPages = [];
          for(let i = this.activePage; i<=this.activePage+2 && i<=this.pages.length; i++)
            this.behindPages.push(i);

          for(let i = this.activePage-1; i>=this.activePage-2 && i>=1; i--)
            this.aheadPages.push(i);

          if(this.behindPages.length<3){
            for(let i = 1; i<=3-this.behindPages.length && this.activePage-2-i>=1; i++)
              this.aheadPages.push(this.activePage-2-i);
          }
          this.aheadPages.reverse();

          if(this.aheadPages.length<3){
            for(let i = 1; i<=3-this.aheadPages.length && this.activePage+2+i<=this.pages.length; i++)
              this.behindPages.push(this.activePage+2+i);
          }
          this.scrollDown();

      }
  }

  scrollDown(){
    let y =  document.querySelector('.event-card')?.getBoundingClientRect().top;
    window.scrollTo({top: 250, behavior: 'smooth'});

  }
}

