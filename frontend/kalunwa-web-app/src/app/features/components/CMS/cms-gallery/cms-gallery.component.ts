import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { GalleryModel } from 'src/app/features/models/CMS/gallery-model';
@Component({
  selector: 'app-cms-gallery',
  templateUrl: './cms-gallery.component.html',
  styleUrls: ['./cms-gallery.component.scss']
})
export class CmsGalleryComponent implements OnInit {

  gallery: GalleryModel[]=[
    {
      id:1,
      image: "assets/images/event.jpg",
    },
    {
      id:2,
      image: "assets/images/event.jpg",
    },
    {
      id:3,
      image: "assets/images/carousel/carousel1.jpg",
    },
    {
      id:4,
      image: "assets/images/carousel/carousel1.jpg",
    },
    {
      id:5,
      image: "assets/images/carousel/carousel1.jpg",
    },
    {
      id:6,
      image: "assets/images/carousel/carousel1.jpg",
    },
  ]
  constructor(private ref: ChangeDetectorRef) { }

  activePage:number = 1;
  currentPage = 0;
  lastPage = 4;

  detectIfChanges(){
    this.ref.detectChanges();
  }

  updateDisplay(newPage:number){
    console.log(newPage,this.activePage);
    this.currentPage += (5*(newPage-this.activePage));
    if(this.currentPage < 0)
      this.currentPage = 0;

    this.lastPage = this.currentPage + 5;
    if(this.lastPage > this.gallery.length)
      this.lastPage = this.gallery.length;

    this.ref.detectChanges();
    this.activePage = newPage;
  }
  ngOnInit(): void {
  }

}
