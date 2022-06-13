import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { NewsletterModel } from 'src/app/features/models/CMS/newsletter-model';
@Component({
  selector: 'app-newsletter',
  templateUrl: './newsletter.component.html',
  styleUrls: ['./newsletter.component.scss']
})
export class NewsletterComponent implements OnInit {

  subscribers: NewsletterModel[]=[
    {
      id: 1,
      first_name: "First Name",
      last_name: "Last Name",
      email: "subscriber1@gmail.com",
      sub_date: new Date(),
    },
    {
      id: 1,
      first_name: "First Name",
      last_name: "Last Name",
      email: "subscriber1@gmail.com",
      sub_date: new Date(),
    },
    {
      id: 1,
      first_name: "First Name",
      last_name: "Last Name",
      email: "subscriber1@gmail.com",
      sub_date: new Date(),
    },
    {
      id: 1,
      first_name: "First Name",
      last_name: "Last Name",
      email: "subscriber1@gmail.com",
      sub_date: new Date(),
    },
    {
      id: 1,
      first_name: "First Name",
      last_name: "Last Name",
      email: "subscriber1@gmail.com",
      sub_date: new Date(),
    },
    {
      id: 1,
      first_name: "First Name",
      last_name: "Last Name",
      email: "subscriber1@gmail.com",
      sub_date: new Date(),
    },
    {
      id: 1,
      first_name: "First Name",
      last_name: "Last Name",
      email: "subscriber1@gmail.com",
      sub_date: new Date(),
    },
    {
      id: 1,
      first_name: "First Name",
      last_name: "Last Name",
      email: "subscriber1@gmail.com",
      sub_date: new Date(),
    },
  ]
  constructor(private ref: ChangeDetectorRef) { }

  activePage:number = 1;
  currentPage = 0;
  lastPage = 5;

  detectIfChanges(){
    this.ref.detectChanges();
  }

  updateDisplay(newPage:number){
    console.log(newPage,this.activePage);
    this.currentPage += (6*(newPage-this.activePage));
    if(this.currentPage < 0)
      this.currentPage = 0;

    this.lastPage = this.currentPage + 6;
    if(this.lastPage > this.subscribers.length)
      this.lastPage = this.subscribers.length;

    this.ref.detectChanges();
    this.activePage = newPage;
    let y =  document.querySelector('.table-content')?.getBoundingClientRect().top;
    window.scrollTo({top: y! + window.scrollY - 80, behavior: 'smooth'});
    console.log(this.currentPage, this.lastPage);
  }

  ngOnInit(): void {
  }

}
