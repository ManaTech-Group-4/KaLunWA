import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class SinglePageService {

  constructor(private http: HttpClient) { }
  
  addJumbo(){
    console.log("jumbotron slide added");
  }
  updateJumbo(){
    console.log("jumbotron slide updated");
  }
  deleteJumbo(){
    console.log("jumbotron slide deleted");
  };

  addMember(){
    console.log("member added");
  }
  updateMember(){
    console.log("member updated");
  }
  deleteMember(){
    console.log("member deleted");
  };
  updateCamp(){
    console.log("camp updated");
  }

  public uploadImage(fileName:string, image:any) {
    const formData = new FormData();

    formData.append("image", image);
    formData.append("name", fileName);
    console.log(image);
    return this.http.post('http://127.0.0.1:8000/api/gallery/', formData);
  }

  printDate(date: Date){
    let month = "";
    switch(date.getMonth()){
      case 1:
        month="January";
        break;
      case 2:
        month="February";
        break;
      case 3:
        month="March";
        break;
      case 4:
        month="April";
        break;
      case 5:
        month="May";
        break;
      case 6:
        month="June";
        break;
      case 7:
        month="July";
        break;
      case 8:
        month="August";
        break;
      case 9:
        month="September";
        break;
      case 10:
        month="October";
        break;
      case 11:
        month="November";
        break;
      case 12:
        month="December";
        break;
    }

    return month + " " + date.getDay() + ", " + date.getFullYear();
  }
}
