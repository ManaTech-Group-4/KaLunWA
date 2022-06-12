import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { CollectivePagesService } from '../../service/collective-pages.service';

@Component({
  selector: 'app-add-collective',
  templateUrl: './add-collective.component.html',
  styleUrls: ['./add-collective.component.scss']
})
export class AddCollectiveComponent implements OnInit {
  collective: FormGroup;
  submitted= false;
  collectiveType: string | null= "project";
  status = "";
  fileName="";
  collection:any;
  profileImage:string;

  constructor(
    private formBuilder: FormBuilder,
    private service: CollectivePagesService,
    private route: ActivatedRoute,
    private router: Router
  ) { }

  ngOnInit(): void {
      this.collective = this.formBuilder.group({
      title: ['',Validators.required],
      start_date: [null],
      end_date: [null],
      camp: ['',Validators.required],
      description: ['',Validators.required],
      image:[null]
    });

    this.collectiveType = this.route.snapshot.paramMap.get("collective-type");
    this.profileImage = "../../assets/images/place.jpg";
  }

  get f() { return this.collective.controls;}

  onSubmit(imageInput:any){
    this.submitted = true;

    if(this.collective.invalid){
      return;
    }

    this.processFile(imageInput);
  }

  private createCollective(id:number){

    let newItem: any;
    if(this.collectiveType != 'news' && this.collectiveType != 'announcements')
      newItem = {
        'title': this.f.title.value,
        'start_date': this.f.start_date.value,
        'end_date': this.f.end_date.value,
        'camp': this.f.camp.value,
        'description': this.f.description.value,
        'image': id
      };

    else
      newItem = {
        'title': this.f.title.value,
        'description': this.f.description.value,
        'image': id
      };


    if(this.collectiveType=="project"){
      const addSubscribe = this.service.addProject(newItem).subscribe(
        suc => {
          console.log('success');
          this.router.navigateByUrl("admin/collective");
          addSubscribe.unsubscribe;
        },
        err => {
          console.log(err);
        }
      );
    }
    if(this.collectiveType=="event"){
      const addSubscribe = this.service.addEvent(newItem).subscribe(
        suc => {
          console.log('success');
          this.router.navigateByUrl("admin/collective");
          addSubscribe.unsubscribe;
        },
        err => {
          console.log(err);
        }
      );
    }
    if(this.collectiveType=="news"){
      const addSubscribe = this.service.addNews(newItem).subscribe(
        suc => {
          console.log('success');
          this.router.navigateByUrl("admin/collective");
          addSubscribe.unsubscribe;
        },
        err => {
          console.log(err);
        }
      );
    }
  }

  updateStatus(){
    let now = new Date();
    if(this.f.start_date.value != null && this.f.end_date.value != null){
      if(this.f.start_date.value > now){
        this.status="Upcoming";
        if(this.f.start_date.value > this.f.endDate.value)
          this.collective.controls["end_date"].setErrors({'incorrect': true});
        else
          this.collective.controls["end_date"].setErrors(null);
      }
      else{
        this.status="Ongoing";
        if(this.f.end_date.value < now )
          this.status="Past";

        if(this.f.start_date.value > this.f.end_date.value)
          this.collective.controls["end_date"].setErrors({'incorrect': true});
        else
          this.collective.controls["end_date"].setErrors(null);
      }
    }
  }

  onFileChange(imageInput:any){
    const file: File = imageInput.target.files[0];
    const reader = new FileReader();
    if(!this.isFileImage(file))
      this.collective.controls["image"].setErrors({'incorrect': true});
    else{
      this.collective.controls["image"].setErrors(null);

      this.fileName = file.name;
    }


    if(imageInput.target.files && imageInput.target.files[0]){
      // File Preview
      reader.readAsDataURL(file);

      reader.onload = () => {
        this.profileImage = reader.result as string;
      }
    }
  }

  processFile(imageInput: any) {
    const file: File = imageInput.files[0];
    const reader = new FileReader();

    if(this.isFileImage(file)){

      reader.addEventListener('load', (event: any) => {

        this.service.uploadImage(this.fileName,file).subscribe(
          (res:any) => {
            this.createCollective(res.id);

          },
          (err) => {
            console.log("Err");
          })
        });

        reader.readAsDataURL(file);
    }
  }

  isFileImage(file: File) {
    return file && file['type'].split('/')[0] === 'image';
  }

  displayDate(date: Date){
    if(!date)
      return "";
    return this.service.printDate(date);
  }


}
