import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { AuditLogsModel } from 'src/app/features/models/CMS/audit-logs-model';

@Component({
  selector: 'app-audit-logs',
  templateUrl: './audit-logs.component.html',
  styleUrls: ['./audit-logs.component.scss']
})
export class AuditLogsComponent implements OnInit {

  logs:AuditLogsModel[]=[
    {
      id: 1,
      administrator: "Name1",
      content_changed: "Homepage-content",
      action: "add something",
      date: "06/08/2021",
      time: "12:51 AM"
    },
    {
      id: 2,
      administrator: "Name2",
      content_changed: "Events-content",
      action: "edit something",
      date: "04/12/2022",
      time: "03:15 PM"
    },
    {
      id: 3,
      administrator: "Name3",
      content_changed: "Projects-content",
      action: "delete something",
      date: "11/21/2021",
      time: "06:25 AM"
    },
    {
      id: 2,
      administrator: "Name2",
      content_changed: "Events-content",
      action: "edit something",
      date: "04/12/2022",
      time: "03:15 PM"
    },
    {
      id: 3,
      administrator: "Name3",
      content_changed: "Projects-content",
      action: "delete something",
      date: "11/21/2021",
      time: "06:25 AM"
    },
    {
      id: 1,
      administrator: "Name1",
      content_changed: "Homepage-content",
      action: "add something",
      date: "06/08/2021",
      time: "12:51 AM"
    },
    {
      id: 2,
      administrator: "Name2",
      content_changed: "Events-content",
      action: "edit something",
      date: "04/12/2022",
      time: "03:15 PM"
    },
    {
      id: 3,
      administrator: "Name3",
      content_changed: "Projects-content",
      action: "delete something",
      date: "11/21/2021",
      time: "06:25 AM"
    },
    {
      id: 2,
      administrator: "Name2",
      content_changed: "Events-content",
      action: "edit something",
      date: "04/12/2022",
      time: "03:15 PM"
    },
    {
      id: 3,
      administrator: "Name3",
      content_changed: "Projects-content",
      action: "delete something",
      date: "11/21/2021",
      time: "06:25 AM"
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
    if(this.lastPage > this.logs.length)
      this.lastPage = this.logs.length;

    this.ref.detectChanges();
    this.activePage = newPage;
    let y =  document.querySelector('.table-content')?.getBoundingClientRect().top;
    window.scrollTo({top: y! + window.scrollY - 80, behavior: 'smooth'});
    console.log(this.currentPage, this.lastPage);
  }

  ngOnInit(): void {
  }

}
