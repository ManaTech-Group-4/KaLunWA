import { Component, OnInit } from '@angular/core';
import { SinglePageListModel } from 'src/app/features/models/CMS/single-page-list-model';
import { SinglePageService } from 'src/app/features/service/single-page.service';

@Component({
  selector: 'app-single-page-list',
  templateUrl: './single-page-list.component.html',
  styleUrls: ['./single-page-list.component.scss']
})
export class SinglePageListComponent implements OnInit {

  selectedCamp: string;
  singlePageList: SinglePageListModel[]=[
    {
      id: 1,
      page: "Homepage",
      status: "Published",
      updated_by: "Admin 1",
      last_updated: "12/11/21",
    },
    {
      id: 2,
      page: "Org Structure",
      status: "Draft",
      updated_by: "Admin 2",
      last_updated: "04/16/21",
    },
    {
      id: 3,
      page: "Baybayon",
      status: "Published",
      updated_by: "Admin 1",
      last_updated: "01/11/21",
    },
    {
      id: 4,
      page: "Lasang",
      status: "Published",
      updated_by: "Admin 1",
      last_updated: "12/11/21",
    },
    {
      id: 5,
      page: "Suba",
      status: "Draft",
      updated_by: "Admin 2",
      last_updated: "04/16/21",
    },
    {
      id: 6,
      page: "Zero Waste",
      status: "Published",
      updated_by: "Admin 1",
      last_updated: "01/11/21",
    },
  ]
  constructor(private service: SinglePageService) { }

  ngOnInit(): void {
  }

}
